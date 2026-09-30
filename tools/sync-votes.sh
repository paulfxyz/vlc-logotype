#!/usr/bin/env sh
# Pull the live public tally from paulfleury.com/vlc and commit it as a ledger snapshot.
# If the host's bot protection blocks curl, download counts.json in a browser and save it to votes/counts.json.
set -e
cd "$(dirname "$0")/.."
tmp="$(mktemp)"
curl -fsSL "https://paulfleury.com/vlc/counts.json?t=$(date +%s)" -o "$tmp"
grep -q '"total_votes"' "$tmp" || { echo "Did not get counts.json (blocked?). Nothing changed."; rm -f "$tmp"; exit 1; }
mv "$tmp" votes/counts.json
git add votes/counts.json
git diff --cached --quiet && { echo "No change in counts."; exit 0; }
git commit -m "votes: snapshot $(date -u +%Y-%m-%dT%H:%MZ) ($(grep -o '"total_votes": [0-9]*' votes/counts.json | grep -o '[0-9]*') votes)"
git push
