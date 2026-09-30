"""Rasterise the SVG icons into ready-to-use files for icon swappers (Replacicon, LiteIcon, Windows, Linux).
  png/macos/<id>.png   1024×1024, transparent (macOS mask with padding and shadow)
  icns/<id>.icns       macOS icon bundle 16–1024 px (for Replacicon, Finder "Get Info" paste)
  ico/<id>.ico         Windows icon 16–256 px (Windows plate)
  png/linux/<id>.png   512×512 (GNOME/Adwaita rounded square)
Needs Playwright + Pillow. Usage: python3 tools/export.py [ids...]"""
import asyncio, io, json, os, sys
from PIL import Image
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(R)
ids = sys.argv[1:] or [d["id"] for d in json.load(open("icons.json"))]
for d in ("png/macos", "png/linux", "icns", "ico"): os.makedirs(d, exist_ok=True)

async def render(page, svg_path, size):
    svg = open(svg_path, encoding="utf-8").read().replace('width="1024" height="1024"', f'width="{size}" height="{size}"', 1)
    await page.set_content(f'<html><body style="margin:0;background:transparent">{svg}</body></html>')
    await page.wait_for_timeout(60)
    png = await page.locator("svg").first.screenshot(omit_background=True)
    return Image.open(io.BytesIO(png)).convert("RGBA")

async def main():
    from playwright.async_api import async_playwright
    exe = os.environ.get("CHROME_PATH")
    async with async_playwright() as p:
        b = await (p.chromium.launch(executable_path=exe) if exe else p.chromium.launch())
        pg = await b.new_page(viewport={"width": 1100, "height": 1100})
        for i in ids:
            mac = await render(pg, f"icons/macos/{i}.svg", 1024)
            mac.save(f"png/macos/{i}.png", optimize=True)
            mac.save(f"icns/{i}.icns", format="ICNS", append_images=[mac.resize((s, s), Image.LANCZOS) for s in (16, 32, 64, 128, 256, 512)])
            win = await render(pg, f"icons/windows/{i}.svg", 256)
            win.save(f"ico/{i}.ico", format="ICO", sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
            lnx = await render(pg, f"icons/linux/{i}.svg", 512)
            lnx.save(f"png/linux/{i}.png", optimize=True)
            print("exported", i, flush=True)
        await b.close()
asyncio.run(main())
