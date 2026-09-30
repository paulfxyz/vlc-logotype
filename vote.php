<?php
// VLC icon vote endpoint — no database. Upload next to index.html via FTP.
// Stores votes in votes.json (make the folder writable by PHP, e.g. chmod 775).
header('Content-Type: application/json');
header('Cache-Control: no-store');
$file = __DIR__ . '/votes.json';
if (!file_exists($file)) file_put_contents($file, '{"votes":{}}');
$fp = fopen($file, 'c+');
flock($fp, LOCK_EX);
$data = json_decode(stream_get_contents($fp), true) ?: ['votes' => []];
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $in = json_decode(file_get_contents('php://input'), true) ?: [];
  $id = preg_replace('/[^0-9]/', '', $in['id'] ?? '');
  $voter = substr(hash('sha256', ($in['voter'] ?? '') . ($_SERVER['REMOTE_ADDR'] ?? '')), 0, 16);
  if ($id !== '' && (int)$id >= 1 && (int)$id <= 50) {
    $list = $data['votes'][$id] ?? [];
    if (($in['action'] ?? 'add') === 'add') { if (!in_array($voter, $list)) $list[] = $voter; }
    else { $list = array_values(array_diff($list, [$voter])); }
    $data['votes'][$id] = $list;
    ftruncate($fp, 0); rewind($fp);
    fwrite($fp, json_encode($data));
  }
}
flock($fp, LOCK_UN); fclose($fp);
$me = substr(hash('sha256', ($_GET['voter'] ?? ($in['voter'] ?? '')) . ($_SERVER['REMOTE_ADDR'] ?? '')), 0, 16);
$mine = [];
foreach ($data['votes'] as $k => $v) if (in_array($me, $v)) $mine[] = (string)$k;
$counts = [];
foreach ($data['votes'] as $k => $v) $counts[$k] = count($v);
echo json_encode(['counts' => (object)$counts, 'mine' => $mine]);
