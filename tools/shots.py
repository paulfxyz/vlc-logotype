"""Export one PNG per concept (all platform mockups).
Run a static server on :8099 in the repo root first:  python3 -m http.server 8099
Then:  pip install playwright && playwright install chromium && python3 tools/shots.py [ids...]
"""
import asyncio,sys
from playwright.async_api import async_playwright
import os
EXE=os.environ.get('CHROME_PATH')  # optional; defaults to Playwright's bundled Chromium
ids=sys.argv[1:] or [f"{i:02d}" for i in range(1,51)]
async def main():
    async with async_playwright() as p:
        b=await (p.chromium.launch(executable_path=EXE) if EXE else p.chromium.launch())
        pg=await b.new_page(viewport={'width':1600,'height':1000},device_scale_factor=1)
        for i in ids:
            await pg.goto(f'http://localhost:8099/index.html?shot={i}'); await pg.wait_for_timeout(400)
            await pg.locator('.shotwrap').screenshot(path=f'shots/{i}.png')
        await b.close()
asyncio.run(main())
