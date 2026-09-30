"""Build i18n/<lang>.json (concept names + descriptions) from i18n/<lang>.txt ("id|name|description" per line)."""
import json, os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ids = [d["id"] for d in json.load(open(os.path.join(ROOT, "icons.json")))]
for src in sorted(glob.glob(os.path.join(ROOT, "i18n", "*.txt"))):
    lang = os.path.basename(src)[:-4]; out = {}
    for line in open(src, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip(): continue
        i, n, d = line.split("|", 2); out[i] = [n, d]
    missing = [i for i in ids if i not in out]
    assert not missing, f"{lang}: missing {missing}"
    json.dump(out, open(os.path.join(ROOT, "i18n", f"{lang}.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print(lang, len(out), "concepts")
