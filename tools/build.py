"""Assemble index.html from tools/index.template.html (mockup CSS and app glyphs live in tools/parts/)."""
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tpl = open(os.path.join(R, "tools/index.template.html"), encoding="utf-8").read()
for key in ("MOCKCSS", "GLYPH"):
    tpl = tpl.replace(f"%%{key}%%", open(os.path.join(R, f"tools/parts/{key.lower()}.txt"), encoding="utf-8").read())
open(os.path.join(R, "index.html"), "w", encoding="utf-8").write(tpl)
print("index.html built")
