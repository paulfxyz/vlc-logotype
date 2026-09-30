"""Regenerate README.md, the banner and the contact sheet from icons.json.
Usage: python3 tools/readme.py [--no-images] [--site]
  --no-images  only rewrite README.md
  --site       also screenshot http://localhost:8099 into .github/img/site.png
Banner/contact sheet need Playwright (CHROME_PATH optional)."""
import json, os, sys, asyncio
from collections import Counter
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
M = json.load(open("icons.json"))
HOL = {"Religious", "National", "Seasonal"}
design = [d for d in M if d["tag"] not in HOL]
holiday = [d for d in M if d["tag"] in HOL]
LIVE = "https://paulfleury.com/vlc/"
ZIP = "https://paulfleury.com/vlc/dump.zip"
REPO = "https://github.com/paulfxyz/vlc-logotype"

def badge(label, msg, color, link, style="flat-square", logo=None, logo_color="ededed"):
    enc = lambda s: quote(s.replace("-", "--").replace("_", "__"), safe="")
    extra = f"&logo={logo}&logoColor={logo_color}" if logo else ""
    return f"[![{label}: {msg}](https://img.shields.io/badge/{enc(label)}-{enc(msg)}-{color}?style={style}&labelColor=282828{extra})]({link})"

def grid(items, cols=5):
    head = "| " + " | ".join([" "] * cols) + " |\n|" + ":-:|" * cols + "\n"
    rows = []
    for k in range(0, len(items), cols):
        cells = [f'<img src="icons/macos/{d["id"]}.svg" width="88" alt="{d["name"]}"><br><b>#{d["id"]}</b> {d["name"]}' for d in items[k:k + cols]]
        cells += [" "] * (cols - len(cells))
        rows.append("| " + " | ".join(cells) + " |")
    return head + "\n".join(rows)

def split_desc(d):
    # holiday descriptions are "When — idea"
    if " — " in d["desc"]:
        when, idea = d["desc"].split(" — ", 1)
        return when, idea
    return "", d["desc"]

def files(d):
    i = d["id"]
    return (f"[macOS](icons/macos/{i}.svg) · [iOS](icons/ios/{i}.svg) · [Android](icons/android/{i}.svg) · "
            f"[Windows](icons/windows/{i}.svg) · [Linux](icons/linux/{i}.svg) · [mockups](shots/{i}.png)")

def md_escape(s): return s.replace("|", "\\|")

tags_design = " · ".join(f"{t} ({n})" for t, n in Counter(d["tag"] for d in design).most_common())
tags_hol = " · ".join(f"{t} ({n})" for t, n in Counter(d["tag"] for d in holiday).most_common())

design_table = "\n".join(f'| `{d["id"]}` | {d["name"]} | {d["tag"]} | {md_escape(d["desc"])} | {files(d)} |' for d in design)
hol_table = "\n".join(f'| `{d["id"]}` | {d["name"]} | {d["tag"]} | {md_escape(split_desc(d)[0])} | {md_escape(split_desc(d)[1])} | {files(d)} |' for d in holiday)

N = len(M)
readme = f'''<div align="center">

<img src=".github/img/banner.png" alt="VLC Logotype: {N} icon concepts for macOS, Windows, iOS, Android and Linux" width="100%">

<br>

**An unofficial redesign study of the [VLC media player](https://www.videolan.org/vlc/) app icon.**<br>
{N} concepts built on Apple's icon grid and adapted to Windows, iOS, Android and Linux, with dock mockups and a tap-to-vote page.

Everything is live at **[paulfleury.com/vlc]({LIVE})**. Prefer not to clone? Grab the whole site in one archive: **[dump.zip]({ZIP})**.

<br>

{badge("license", "MIT", "0a0a0a", "LICENSE", "for-the-badge")}
{badge("live", "paulfleury.com/vlc", "ff7a00", LIVE, "for-the-badge")}
{badge("download", "dump.zip", "0a0a0a", ZIP, "for-the-badge")}

{badge("concepts", str(N), "ff7a00", "#-the-concepts")}
{badge("design directions", str(len(design)), "0a0a0a", "#-design-directions")}
{badge("holiday editions", str(len(holiday)), "0a0a0a", "#-holiday-editions")}
{badge("macOS", "824/1024 squircle", "0a0a0a", "#-platform-exports", logo="apple")}
{badge("iOS", "full-bleed", "0a0a0a", "#-platform-exports", logo="apple")}
{badge("Android", "adaptive circle", "3ddc84", "#-platform-exports", logo="android")}
{badge("Windows", "Fluent plate", "0078d4", "#-platform-exports")}
{badge("Linux", "GNOME dash", "0a0a0a", "#-platform-exports", logo="linux")}
{badge("icons", "SVG", "ffb13b", "icons/")}
{badge("mockups", f"{N} PNG", "0a0a0a", "shots/")}
{badge("votes", "no database", "ff7a00", "#-voting-without-a-database")}
{badge("vote ledger", "counts.json", "0a0a0a", "votes/counts.json")}
{badge("dependencies", "0", "0a0a0a", "#-stack")}
{badge("build step", "none", "0a0a0a", "#-run-it-locally")}
{badge("PHP", "vote endpoint", "777bb4", "vote.php", logo="php")}
{badge("JavaScript", "vanilla", "f7df1e", "index.html", logo="javascript", logo_color="282828")}
{badge("i18n", "EN · FR · ES · PT", "0a0a0a", "i18n/")}
{badge("theme", "light · dark", "0a0a0a", "#-the-site")}
{badge("Python", "generator", "3776ab", "tools/gen.py", logo="python")}
{badge("vibe designed", "Perplexity Computer", "20808d", "#-this-is-vibe-designing", logo="perplexity")}

**[→ Open the voting page]({LIVE})** &nbsp;·&nbsp; **[→ The concepts](#-the-concepts)** &nbsp;·&nbsp; **[→ Why redesign it](#-why-redesign-it)** &nbsp;·&nbsp; **[↓ Download](ZIP_PLACEHOLDER)**

</div>

---

## 📋 Summary

On macOS, VLC ships a bare traffic cone with no background plate. Every other app in the Dock sits on the same rounded square, so VLC looks smaller, off-grid and slightly out of place, especially since macOS 26 Tahoe.

This repository is a free, unsolicited proposal to fix that.

| # | Deliverable | What it is | Where |
|---|---|---|---|
| **1** | **{N} icon concepts** | {len(design)} design directions, from a faithful refresh to bolder ideas, plus {len(holiday)} holiday editions | [`icons/`](icons/) |
| **2** | **Platform exports** | Every concept as SVG with the macOS, iOS, Android, Windows and Linux masks, plus raw background and foreground layers | [`icons/<platform>/`](icons/) |
| **3** | **Dock mockups** | macOS Dock, before/after, Windows 11 taskbar, iOS and Android home screens, GNOME dash | [`shots/`](shots/) |
| **4** | **Voting page** | One static `index.html`: open a concept, see it in every dock, vote. No database | [paulfleury.com/vlc]({LIVE}) |

> [!NOTE]
> Concept work, not affiliated with or endorsed by VideoLAN. "VLC" and the cone are trademarks of VideoLAN. The MIT License covers the code and tooling in this repository.

---

## 🌐 The site

<div align="center"><a href="{LIVE}"><picture><source media="(prefers-color-scheme: light)" srcset=".github/img/site-light.png"><img src=".github/img/site.png" alt="The voting page at paulfleury.com/vlc showing {N} concepts" width="100%"></picture></a></div>

Open any concept to see it in the macOS Dock, a before/after, the Windows 11 taskbar, iOS and Android home screens and the GNOME dash, then vote. Filters split the {len(design)} design directions from the {len(holiday)} holiday editions. The page has a light and dark mode (it follows your system on first visit) and is fully translated into English, French, Spanish and European Portuguese, concept names and descriptions included.

---

## 🔍 Why redesign it

<div align="center"><img src=".github/img/mockups-30.png" alt="Concept #30 in the macOS Dock, Windows taskbar, GNOME dash, iOS and Android" width="100%"></div>

- **Squircle plate.** An 824 px body on a 1024 px canvas with continuous corners, like every native macOS app.
- **Optical balance.** The cone fills about 60% of the plate, so it carries the same visual weight as its neighbours.
- **Depth, not clutter.** Soft top-lit gradients and a single drop shadow, following Tahoe's layered-icon direction.
- **One source, five masks.** Background and foreground are separate layers, so each platform gets its own correct shape.

---

## 🎨 The concepts

<div align="center"><img src=".github/img/contact-sheet.png" alt="Contact sheet of all {N} concepts" width="100%"></div>

### 🧭 Design directions

{len(design)} directions: {tags_design}.

{grid(design)}

<details>
<summary><b>All {len(design)} design directions, with descriptions and downloads</b></summary>

| # | Name | Family | Idea | Files |
|---|---|---|---|---|
{design_table}

</details>

### 🎉 Holiday editions

{len(holiday)} seasonal variants for the dates people actually celebrate: {tags_hol}. Religious symbols are kept to widely shared, respectful motifs (lights, lanterns, crescents, arches, lotus); no figures are depicted.

<div align="center"><img src=".github/img/mockups-66.png" alt="Holiday edition #66 Halloween in every dock" width="100%"></div>

{grid(holiday)}

<details>
<summary><b>All {len(holiday)} holiday editions, with dates and downloads</b></summary>

| # | Name | Type | When | Idea | Files |
|---|---|---|---|---|---|
{hol_table}

</details>

---

## 🧩 Platform exports

| Platform | Folder | Shape |
|---|---|---|
| macOS | [`icons/macos/`](icons/macos/) | 824/1024 squircle with padding, rim light and drop shadow (Apple grid) |
| iOS / iPadOS | [`icons/ios/`](icons/ios/) | Full-bleed squircle; the system applies its own mask |
| Android | [`icons/android/`](icons/android/) | Adaptive icon preview, circle mask |
| Windows 11 | [`icons/windows/`](icons/windows/) | Fluent-style rounded plate |
| Linux (GNOME) | [`icons/linux/`](icons/linux/) | Adwaita-style rounded square |
| Layers | [`icons/layers-bg/`](icons/layers-bg/) · [`icons/layers-fg/`](icons/layers-fg/) | Raw background and foreground, for Icon Composer or Android adaptive icons |

---

## 📮 Voting without a database

Open a concept, check it in every dock, then tap **Vote**. Tap again to undo. Each browser gets a random voter ID in a cookie, and the server keeps one vote per voter per concept.

| Backend | File | Storage |
|---|---|---|
| Any PHP host (FTP) | [`vote.php`](vote.php) | Private `votes.private.php` (guarded, never served) plus public `counts.json`, both written under a file lock |
| Vercel | [`api/votes.js`](api/votes.js) | Vercel Blob, one empty file per vote (`votes/<id>/<voter>`), counted by listing |
| Local or any VPS | [`server/server.py`](server/server.py) | `data/votes.json`, Python standard library only |

The page picks the endpoint on its own: `vote.php` by default, `/api/votes` on `*.vercel.app`. To point it anywhere else, set `window.VOTE_API` before the main script.

### 🔗 The vote ledger

The tally is public at every step, with GitHub as the audit trail:

1. Every vote rewrites **[counts.json]({LIVE}counts.json)** on the live site: counts per concept, total votes, unique voters, a UTC timestamp and `ledger_sha256`, a hash of the private ballot file.
2. The private ballot file (`votes.private.php`) holds only pseudonymous hashes and is never served: a PHP guard line returns 404 and `.htaccess` denies it.
3. Snapshots of `counts.json` are committed to **[votes/counts.json](votes/counts.json)** with [`tools/sync-votes.sh`](tools/sync-votes.sh). The commit history is the ledger: anyone can diff two snapshots and see exactly how the count moved.

> [!WARNING]
> Votes are anonymous and unauthenticated. The voter ID is hashed together with the IP address, which makes ballot-stuffing harder but not impossible. Treat the tally as a signal, not a poll.

---

## 🚀 Deploy

**FTP or shared hosting (what runs [paulfleury.com/vlc]({LIVE}))**

1. Upload `index.html`, `icons.json`, `icons/`, `i18n/`, `shots/`, `vote.php`, `.htaccess`, `og.png` and optionally `dump.zip` to one folder.
2. Make sure PHP can write to that folder, so `votes.private.php` and `counts.json` can be created on the first vote.

**Vercel**

```bash
vercel link
vercel blob create-store vlc-logotype   # connect it to the project so BLOB_READ_WRITE_TOKEN is set
vercel deploy --prod
```

---

## 💻 Run it locally

```bash
python3 server/server.py &    # optional vote API on :8787
python3 -m http.server 8099   # then open http://localhost:8099
```

Without a reachable vote endpoint, the page still works and keeps votes for the current visit only.

---

## 🤖 This is vibe designing

No design tool was opened for this project. Every icon, mockup and page was designed through conversation: Paul described the problem (VLC's cone floating off-grid in the macOS Dock), set direction and taste, and asked for more ("30 options", "push it to 50", "add 50 holidays"). An AI agent turned each request into code, rendered it, looked at the result and iterated.

- **No image generator.** Each concept is hand-written SVG geometry produced as code in [`tools/gen.py`](tools/gen.py), so every icon is crisp at any size, editable, diffable and reproducible.
- **Look, then fix.** The agent rendered contact sheets and platform mockups in a headless browser, reviewed them visually, and corrected what looked wrong, for example rebuilding the voxel cone, which first came out as a column instead of a pyramid.
- **Human in the loop.** Scope, taste and every publish step came from Paul; the agent handled drafting, building, QA and shipping.

| Role | Model / tool |
|---|---|
| Agent platform | [Perplexity Computer](https://www.perplexity.ai/computer) |
| Design, SVG, code, README, QA | Claude Opus 5.5 (Anthropic), the orchestrating model |
| Pre-publish security review | GPT-6 Luna (OpenAI) |
| Rendering and screenshots | Chromium via [Playwright](https://playwright.dev) |
| Badges | [shields.io](https://shields.io) |

---

## 🧰 Stack

- **Icons**: hand-written SVG generated by [`tools/gen.py`](tools/gen.py), Python standard library only. Edit a concept, run `python3 tools/gen.py`, and every platform export updates.
- **Mockups**: plain HTML and CSS inside [`index.html`](index.html). `?shot=<id>` renders the export layout.
- **Screenshots**: [`tools/shots.py`](tools/shots.py), with Playwright.
- **README, banner and contact sheet**: [`tools/readme.py`](tools/readme.py) rebuilds all three from `icons.json`.
- **Page**: one file, vanilla JavaScript, no framework. [`tools/build.py`](tools/build.py) assembles `index.html` from [`tools/index.template.html`](tools/index.template.html); the output is committed, so there is nothing to build to run it.
- **Translations**: UI strings live in the page; concept names and descriptions live in [`i18n/`](i18n/) as `id|name|description` text files, compiled to JSON by [`tools/i18n.py`](tools/i18n.py), which fails if any concept is missing.

```
index.html          voting page and all dock mockups
icons.json          concept registry (id, name, family, description)
icons/<platform>/   {N} SVGs per platform, plus raw layers
shots/              {N} PNG mockup sheets
i18n/               fr · es · pt translations (text source + JSON)
vote.php            PHP vote endpoint (FTP hosting)
votes/counts.json   committed snapshots of the public tally (the ledger)
api/votes.js        Vercel function (Vercel Blob)
server/server.py    standalone Python vote server
tools/              gen.py · shots.py · build.py · i18n.py · readme.py · sync-votes.sh
```

---

## 📄 License

Released under the [MIT License](LICENSE). "VLC" and the VLC cone are trademarks of VideoLAN; this is an independent design proposal.
'''.replace("ZIP_PLACEHOLDER", ZIP)
open("README.md", "w").write(readme)
print("README.md written")

if "--no-images" in sys.argv:
    sys.exit()

icons = "".join(f'<img src="../../icons/macos/{d["id"]}.svg">' for d in M)
banner = f"""<html><body style="margin:0;width:1280px;height:640px;background:radial-gradient(120% 90% at 20% 0%,#3A2CB8 0,#140D45 55%,#0B0820 100%);font-family:-apple-system,Inter,Helvetica,Arial,sans-serif;color:#fff;overflow:hidden;position:relative">
<div style="position:absolute;left:72px;top:64px;display:flex;align-items:center;gap:28px"><img src="../../icons/macos/30.svg" width="150"><div>
<div style="font-size:18px;letter-spacing:.14em;color:#FF9A3C;font-weight:700">UNOFFICIAL REDESIGN STUDY</div>
<div style="font-size:78px;font-weight:800;letter-spacing:-.02em;line-height:1.02">VLC Logotype</div>
<div style="font-size:25px;color:#C9C6E8;margin-top:8px">{N} icon concepts · macOS · Windows · iOS · Android · Linux</div></div></div>
<div style="position:absolute;left:50%;bottom:36px;transform:translateX(-50%);padding:14px 18px;border-radius:26px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.25)">
<style>img{{display:block}} .d img{{width:40px;height:40px}}</style><div class="d" style="display:grid;grid-template-columns:repeat(25,40px);gap:6px">{icons}</div></div></body></html>"""
sheet = ('<html><body style="margin:0;background:#0E0E10;display:grid;grid-template-columns:repeat(10,150px);gap:14px 10px;padding:26px;width:1590px;'
         'font:13px -apple-system,Inter,Arial,sans-serif;color:#E4E4E7">' + "".join(
    f'<div style="text-align:center"><img src="../../icons/macos/{d["id"]}.svg" width="120" style="display:block;margin:0 auto 4px">#{d["id"]} {d["name"]}</div>' for d in M) + "</body></html>")
os.makedirs(".github/img", exist_ok=True)
open(".github/img/_banner.html", "w").write(banner); open(".github/img/_sheet.html", "w").write(sheet)

async def render():
    from playwright.async_api import async_playwright
    exe = os.environ.get("CHROME_PATH")
    async with async_playwright() as p:
        b = await (p.chromium.launch(executable_path=exe) if exe else p.chromium.launch())
        base = "file://" + os.path.join(ROOT, ".github/img/")
        pg = await b.new_page(viewport={"width": 1280, "height": 640}, device_scale_factor=2)
        await pg.goto(base + "_banner.html"); await pg.wait_for_timeout(800); await pg.screenshot(path=".github/img/banner.png")
        pg2 = await b.new_page(viewport={"width": 1642, "height": 900})
        await pg2.goto(base + "_sheet.html"); await pg2.wait_for_timeout(800); await pg2.screenshot(path=".github/img/contact-sheet.png", full_page=True)
        if "--site" not in sys.argv:
            await b.close(); return
        pg3 = await b.new_page(viewport={"width": 1440, "height": 1100}, device_scale_factor=1)
        try:
            await pg3.goto("http://localhost:8099/index.html"); await pg3.wait_for_timeout(1500)
            await pg3.evaluate("window.scrollTo(0, 0)"); await pg3.screenshot(path=".github/img/site.png")
        except Exception as e:
            print("site.png skipped (serve the repo on :8099 first):", e)
        await b.close()
asyncio.run(render())
os.remove(".github/img/_banner.html"); os.remove(".github/img/_sheet.html")
print("banner.png and contact-sheet.png written")
