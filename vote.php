<?php
// VLC Logotype vote endpoint: no database. Upload next to index.html via FTP.
// Private ledger: votes.private.php (pseudonymous voter hashes; a PHP guard line stops direct download).
// Public tally:   counts.json (counts only), rewritten after every vote and mirrored to GitHub (votes/counts.json).
header('Content-Type: application/json');
header('Cache-Control: no-store');
const MAX_ID = 100;
$file   = __DIR__ . '/votes.private.php';
$public = __DIR__ . '/counts.json';
$guard  = "<?php http_response_code(404); exit; ?>\n";

$fp = fopen($file, 'c+');
flock($fp, LOCK_EX);
$raw  = stream_get_contents($fp);
$json = strpos($raw, $guard) === 0 ? substr($raw, strlen($guard)) : $raw;
$data = json_decode($json, true) ?: ['votes' => []];
$in   = [];
$changed = false;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $in = json_decode(file_get_contents('php://input'), true) ?: [];
  $n  = (int)preg_replace('/[^0-9]/', '', (string)($in['id'] ?? ''));
  $voter = substr((string)($in['voter'] ?? ''), 0, 64);
  if ($n >= 1 && $n <= MAX_ID && $voter !== '') {
    $id = str_pad((string)$n, 2, '0', STR_PAD_LEFT);
    $me = substr(hash('sha256', $voter . ($_SERVER['REMOTE_ADDR'] ?? '')), 0, 16);
    $list = $data['votes'][$id] ?? [];
    if (($in['action'] ?? 'add') === 'add') { if (!in_array($me, $list, true)) { $list[] = $me; $changed = true; } }
    else { $before = count($list); $list = array_values(array_diff($list, [$me])); $changed = $before !== count($list); }
    $data['votes'][$id] = $list;
    if (!$list) unset($data['votes'][$id]);
  }
}

ksort($data['votes']);
$counts = [];
foreach ($data['votes'] as $k => $v) $counts[(string)$k] = count($v);
$body = json_encode($data);

if ($changed || !file_exists($public) || $raw === '') {
  ftruncate($fp, 0); rewind($fp); fwrite($fp, $guard . $body); fflush($fp);
  $pub = [
    'project'       => 'VLC Logotype',
    'source'        => 'https://github.com/paulfxyz/vlc-logotype',
    'updated_at'    => gmdate('c'),
    'total_votes'   => array_sum($counts),
    'voters'        => count(array_unique(array_merge([], ...array_values($data['votes'] ?: [[]])))),
    'counts'        => (object)$counts,
    'ledger_sha256' => hash('sha256', $body),
  ];
  file_put_contents($public, json_encode($pub, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES) . "\n", LOCK_EX);
}
flock($fp, LOCK_UN); fclose($fp);

$vid  = (string)($_GET['voter'] ?? ($in['voter'] ?? ''));
$me   = $vid !== '' ? substr(hash('sha256', substr($vid, 0, 64) . ($_SERVER['REMOTE_ADDR'] ?? '')), 0, 16) : '';
$mine = [];
if ($me !== '') foreach ($data['votes'] as $k => $v) if (in_array($me, $v, true)) $mine[] = (string)$k;
echo json_encode(['counts' => (object)$counts, 'mine' => $mine]);
