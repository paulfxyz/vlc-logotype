# Same API as vote.php, for the pplx.app preview (stores votes in votes.json)
import json, hashlib, os, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data'); os.makedirs(D, exist_ok=True); F = os.path.join(D, 'votes.json'); L = threading.Lock()
def load():
    try: return json.load(open(F))
    except Exception: return {"votes": {}}
def h(x): return hashlib.sha256(str(x).encode()).hexdigest()[:16]
def counts(d, me=None): return {"counts": {k: len(v) for k, v in d["votes"].items()}, "mine": [k for k, v in d["votes"].items() if me and me in v]}
class H(BaseHTTPRequestHandler):
    def _send(self, obj):
        b = json.dumps(obj).encode(); self.send_response(200)
        for k, v in [("Content-Type","application/json"),("Access-Control-Allow-Origin","*"),("Access-Control-Allow-Headers","Content-Type"),("Cache-Control","no-store")]: self.send_header(k, v)
        self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_OPTIONS(self): self._send({})
    def do_GET(self):
        from urllib.parse import urlparse, parse_qs
        q = parse_qs(urlparse(self.path).query); me = h(q.get("voter", [""])[0])
        with L: self._send(counts(load(), me))
    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0) or 0)
        try: i = json.loads(self.rfile.read(n) or b"{}")
        except Exception: i = {}
        vid = "".join(c for c in str(i.get("id", "")) if c.isdigit())
        voter = h(i.get("voter", ""))
        with L:
            d = load()
            if vid and 1 <= int(vid) <= 100:
                lst = d["votes"].get(vid, [])
                if i.get("action", "add") == "add":
                    if voter not in lst: lst.append(voter)
                else: lst = [v for v in lst if v != voter]
                d["votes"][vid] = lst; json.dump(d, open(F, "w"))
            self._send(counts(d, voter))
    def log_message(self, *a): pass
ThreadingHTTPServer(("0.0.0.0", 8787), H).serve_forever()
