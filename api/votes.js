// Vercel function: file-per-vote storage in Vercel Blob (no database).
// Each vote is an empty blob at votes/<iconId>/<voterHash>; counts = list by prefix.
import { put, del, list } from '@vercel/blob';
import crypto from 'node:crypto';

const hash = (s) => crypto.createHash('sha256').update(s).digest('hex').slice(0, 16);

async function tally(me) {
  const counts = {}, mine = [];
  let cursor;
  do {
    const r = await list({ prefix: 'votes/', cursor, limit: 1000 });
    for (const b of r.blobs) {
      const [, id, voter] = b.pathname.split('/');
      if (!id || !voter) continue;
      counts[id] = (counts[id] || 0) + 1;
      if (me && voter === me) mine.push(id);
    }
    cursor = r.hasMore ? r.cursor : undefined;
  } while (cursor);
  return { counts, mine };
}

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  const ip = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim();
  try {
    if (req.method === 'GET') {
      const v = String(req.query.voter || '');
      return res.status(200).json(await tally(v ? hash(v + ip) : null));
    }
    if (req.method === 'POST') {
      const body = typeof req.body === 'string' ? JSON.parse(req.body || '{}') : (req.body || {});
      const n = parseInt(String(body.id || '').replace(/\D/g, ''), 10);
      const id = String(n).padStart(2, '0');
      const rawVoter = String(body.voter || '').slice(0, 64);
      if (!(n >= 1 && n <= 100) || !rawVoter) return res.status(400).json({ error: 'bad request' });
      const me = hash(rawVoter + ip);
      const path = `votes/${id}/${me}`;
      if (body.action === 'remove') {
        const r = await list({ prefix: path, limit: 1 });
        if (r.blobs.length) await del(r.blobs.map((b) => b.url));
      } else {
        await put(path, '1', { access: 'public', addRandomSuffix: false, allowOverwrite: true, contentType: 'text/plain' });
      }
      return res.status(200).json(await tally(me));
    }
    res.setHeader('Allow', 'GET, POST');
    return res.status(405).json({ error: 'method not allowed' });
  } catch (e) {
    return res.status(500).json({ error: 'storage error' });
  }
}
