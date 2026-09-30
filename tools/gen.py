"""Generate 30 VLC icon concepts as layered SVGs (background + foreground),
exported per platform mask: macOS (squircle w/ padding + shadow), iOS (full-bleed
squircle), Android (adaptive circle), Windows (Fluent free-form fg on soft plate),
Linux (GNOME/Adwaita rounded-square), plus raw layers."""
import math, json, os

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
S = 1024

def squircle(cx, cy, r, n=5.0, steps=160):
    pts = []
    for i in range(steps):
        t = 2 * math.pi * i / steps
        c, s = math.cos(t), math.sin(t)
        x = cx + r * math.copysign(abs(c) ** (2 / n), c)
        y = cy + r * math.copysign(abs(s) ** (2 / n), s)
        pts.append(f"{x:.1f},{y:.1f}")
    return "M" + " L".join(pts) + " Z"

SQ_FULL = squircle(512, 512, 512)
SQ_MAC = squircle(512, 512, 412)   # 824px body on 1024 canvas (Apple grid)

# ---------- cone primitives (1024 space, centred) ----------
def cone_path(tip=250, base=700, half=178, tipw=24):
    l, r = 512 - half, 512 + half
    return (f"M{512-tipw},{tip+14} Q512,{tip-10} {512+tipw},{tip+14} "
            f"L{r},{base} L{l},{base} Z")

CONE = cone_path()
STRIPES = [(395, 455), (545, 610)]

def base_shape(y=690, h=78, w=470, rx=26):
    return f'<rect x="{512-w/2}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'

def cone(uid, body, stripe, basefill, shade=True, stroke=None, sw=0,
         cone_d=CONE, stripes=STRIPES, base=None, gloss=False, extra=""):
    base = base or base_shape()
    st = f' stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"' if stroke else ""
    s = f'<clipPath id="cc{uid}"><path d="{cone_d}"/></clipPath>'
    s += f'<g fill="{basefill}"{st}>{base}</g>'
    s += f'<path d="{cone_d}" fill="{body}"{st}/>'
    s += f'<g clip-path="url(#cc{uid})" fill="{stripe}">' + "".join(
        f'<rect x="0" y="{a}" width="1024" height="{b-a}"/>' for a, b in stripes) + "</g>"
    if shade:
        s += (f'<linearGradient id="sh{uid}" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".22"/>'
              f'<stop offset=".38" stop-color="#fff" stop-opacity=".18"/><stop offset=".55" stop-color="#fff" stop-opacity="0"/>'
              f'<stop offset="1" stop-color="#000" stop-opacity=".28"/></linearGradient>'
              f'<path d="{cone_d}" fill="url(#sh{uid})"/>')
    if gloss:
        s += (f'<linearGradient id="gl{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".75"/>'
              f'<stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
              f'<path d="M478,290 Q500,262 512,262 L470,520 L430,520 Z" fill="url(#gl{uid})" opacity=".7"/>')
    return s + extra

def lg(uid, c1, c2, x1=0, y1=0, x2=0, y2=1):
    return (f'<linearGradient id="{uid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>')

def rg(uid, c1, c2, cx=.5, cy=.35, r=.8):
    return (f'<radialGradient id="{uid}" cx="{cx}" cy="{cy}" r="{r}">'
            f'<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></radialGradient>')

def bg_grad(uid, c1, c2, kind="lg"):
    g = lg(f"b{uid}", c1, c2) if kind == "lg" else rg(f"b{uid}", c1, c2)
    return g + f'<rect width="1024" height="1024" fill="url(#b{uid})"/>'

def soft_shadow(uid, dy=26, blur=22, op=.35):
    return (f'<filter id="ds{uid}" x="-30%" y="-30%" width="160%" height="160%">'
            f'<feDropShadow dx="0" dy="{dy}" stdDeviation="{blur}" flood-color="#000" flood-opacity="{op}"/></filter>')

OR, OR2, OR_D = "#FF8A00", "#FF5E00", "#D84A00"
designs = []
def add(name, desc, bg, fg, tag):
    designs.append(dict(name=name, desc=desc, bg=bg, fg=fg, tag=tag))

# 1 Faithful refresh
i = 1
add("Faithful Refresh", "The current cone, finally sitting on a proper macOS squircle with a warm off-white plate.",
    bg_grad(i, "#FFFFFF", "#ECE7E1"),
    soft_shadow(i, 18, 16, .25) + f'<g filter="url(#ds{i})">' + cone(i, OR, "#fff", OR_D) + "</g>", "Classic")
# 2 Orange plate, white cone
i = 2
add("Inverted Orange", "Brand orange becomes the plate; a crisp white cone with orange stripes.",
    bg_grad(i, "#FFA531", "#FF5B00"),
    soft_shadow(i, 20, 18, .28) + f'<g filter="url(#ds{i})">' + cone(i, "#fff", "#FF7A00", "#F3EEE9", shade=False) + "</g>", "Bold")
# 3 Graphite
i = 3
add("Graphite Pro", "Pro-app dark graphite plate (think Final Cut / Logic) with a luminous cone.",
    bg_grad(i, "#3A3D44", "#15161A"),
    soft_shadow(i, 16, 20, .6) + f'<g filter="url(#ds{i})">' + cone(i, OR, "#fff", "#C24400", gloss=True) + "</g>", "Pro")
# 4 Liquid glass
i = 4
add("Liquid Glass", "macOS Tahoe style: frosted translucent cone floating over a warm gradient field.",
    bg_grad(i, "#FFB347", "#FF6A00") + '<circle cx="300" cy="260" r="260" fill="#fff" opacity=".18"/>',
    soft_shadow(i, 24, 26, .25) +
    f'<g filter="url(#ds{i})">' + cone(i, "rgba(255,255,255,.55)", "rgba(255,255,255,.9)", "rgba(255,255,255,.6)",
                                    stroke="rgba(255,255,255,.95)", sw=6, gloss=True) + "</g>", "Tahoe")
# 5 Flat minimal
i = 5
add("Flat Minimal", "One colour, one shape. White silhouette with a single negative stripe.",
    f'<rect width="1024" height="1024" fill="{OR2}"/>',
    cone(i, "#fff", OR2, "#fff", shade=False, stripes=[(470, 530)]), "Minimal")
# 6 Sunset
i = 6
add("Sunset", "Orange-to-magenta evening gradient, playful and modern.",
    bg_grad(i, "#FFB000", "#E0206A"),
    soft_shadow(i, 20, 18, .3) + f'<g filter="url(#ds{i})">' + cone(i, "#fff", "#FF5A3C", "#FDE7DD", shade=False) + "</g>", "Bold")
# 7 Play cut-out
i = 7
add("Play Cone", "The cone's middle stripe is replaced by a play triangle: media player at a glance.",
    bg_grad(i, "#FFFFFF", "#F0EBE6"),
    soft_shadow(i, 18, 16, .25) + f'<g filter="url(#ds{i})">' + cone(i, OR, "#fff", OR_D, stripes=[(380, 430)]) +
    '<path d="M470,480 L585,555 L470,630 Z" fill="#fff" stroke="#fff" stroke-width="14" stroke-linejoin="round"/></g>', "Concept")
# 8 Neumorphic
i = 8
add("Soft Neumorphic", "Embossed cone pressed out of a pale warm surface.",
    bg_grad(i, "#F6F1EC", "#E4DCD3"),
    '<filter id="nm8"><feDropShadow dx="-18" dy="-18" stdDeviation="18" flood-color="#fff" flood-opacity=".9"/>'
    '<feDropShadow dx="20" dy="22" stdDeviation="22" flood-color="#A8988A" flood-opacity=".6"/></filter>'
    '<g filter="url(#nm8)">' + cone(i, "#F2ECE6", "#FF7A00", "#EFE8E1", shade=False) + "</g>", "Soft")
# 9 Isometric
i = 9
iso_cone = "M512,210 L690,690 Q512,760 334,690 Z"
add("Round 3D", "A true conical body with curved stripes and elliptical base.",
    bg_grad(i, "#FFFFFF", "#E9E4DE"),
    soft_shadow(i, 24, 22, .3) + lg("ib9", "#B63C00", "#FF9A2E", 0, 0, 1, 0) +
    f'<g filter="url(#ds{i})"><ellipse cx="512" cy="712" rx="250" ry="70" fill="{OR_D}"/>'
    f'<ellipse cx="512" cy="700" rx="250" ry="70" fill="{OR}"/>'
    f'<clipPath id="cc9"><path d="{iso_cone}"/></clipPath><path d="{iso_cone}" fill="{OR}"/>'
    '<g clip-path="url(#cc9)" fill="#fff"><path d="M0,390 Q512,450 1024,390 L1024,445 Q512,510 0,445Z"/>'
    '<path d="M0,540 Q512,610 1024,540 L1024,605 Q512,680 0,605Z"/></g>'
    f'<linearGradient id="sh9" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".3"/><stop offset=".35" stop-color="#fff" stop-opacity=".25"/>'
    f'<stop offset=".6" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".35"/></linearGradient>'
    f'<path d="{iso_cone}" fill="url(#sh9)"/></g>', "3D")
# 10 SF line
i = 10
add("SF Line", "SF Symbols-style monoline cone in white on orange; ultra-legible at 16px.",
    bg_grad(i, "#FF9A1F", "#FF6200"),
    f'<g fill="none" stroke="#fff" stroke-width="44" stroke-linejoin="round" stroke-linecap="round">'
    f'<path d="{cone_path(270, 690, 170)}"/><path d="M300,720 H724"/><path d="M430,450 H594"/><path d="M395,570 H629"/></g>', "Minimal")
# 11 Pixel
i = 11
px = ""
rows = ["....##....", "....##....", "...####...", "...wwww...", "..######..", "..######..", ".wwwwwwww.", ".########.", "##########", "OOOOOOOOOO"]
for r, row in enumerate(rows):
    for c, ch in enumerate(row):
        col = {"#": OR, "w": "#fff", "O": OR_D}.get(ch)
        if col:
            px += f'<rect x="{212+c*60}" y="{212+r*60}" width="60" height="60" fill="{col}"/>'
add("8-Bit", "Retro pixel-art cone for the nostalgic. Crisp at every integer scale.",
    '<rect width="1024" height="1024" fill="#1B1B2F"/>' + "".join(
        f'<rect x="{x}" y="{y}" width="8" height="8" fill="#fff" opacity=".5"/>' for x, y in [(150, 170), (860, 240), (800, 830), (180, 820), (700, 150)]),
    px, "Retro")
# 12 Film ring
i = 12
holes = "".join(f'<rect x="{512+math.cos(a)*330-14:.0f}" y="{512+math.sin(a)*330-14:.0f}" width="28" height="28" rx="6" '
                f'transform="rotate({math.degrees(a):.0f} {512+math.cos(a)*330:.0f} {512+math.sin(a)*330:.0f})" fill="#2A2A2A"/>'
                for a in [k * 2 * math.pi / 24 for k in range(24)])
add("Film Reel", "The cone sits inside a film-reel ring, nodding to VLC's cinema roots.",
    bg_grad(i, "#2A2A2E", "#111113"),
    f'<circle cx="512" cy="512" r="360" fill="none" stroke="{OR}" stroke-width="70"/>' + holes +
    cone(i, OR, "#fff", OR_D, cone_d=cone_path(300, 640, 140), stripes=[(420, 465), (530, 580)],
         base=base_shape(630, 60, 360, 20)), "Concept")
# 13 Blueprint
i = 13
grid = "".join(f'<path d="M{k},0 V1024 M0,{k} H1024" stroke="#fff" stroke-opacity=".12" stroke-width="3"/>' for k in range(64, 1024, 64))
add("Blueprint", "Technical drawing of the cone on blueprint paper. For the engineers.",
    f'<rect width="1024" height="1024" fill="#1E5AA8"/>' + grid,
    f'<g fill="none" stroke="#fff" stroke-width="18" stroke-linejoin="round"><path d="{CONE}"/>{base_shape().replace("/>"," fill=\"none\"/>")}'
    '<path d="M424,455 H600 M378,545 H646 M372,610 H652 M404,395 H620" stroke-width="10"/></g>'
    f'<path d="M760,250 V700 M745,250 H775 M745,700 H775" stroke="{OR}" stroke-width="8"/>', "Concept")
# 14 Neon night
i = 14
add("Neon Night", "Glowing neon-tube cone on midnight navy. Pops in a dark dock.",
    bg_grad(i, "#141B3A", "#070A18"),
    '<filter id="gw14" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="14" result="b"/>'
    '<feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
    f'<g filter="url(#gw14)" fill="none" stroke="#FF9A3C" stroke-width="26" stroke-linejoin="round" stroke-linecap="round">'
    f'<path d="{cone_path(270, 690, 170)}"/><path d="M310,730 H714"/><path d="M430,450 H594" stroke="#FFE3C4"/><path d="M395,570 H629" stroke="#FFE3C4"/></g>', "Dark")
# 15 Mono tinted
i = 15
add("Mono Tint", "Built for macOS/iOS tinted & clear modes: pure greyscale that adapts to any accent.",
    bg_grad(i, "#5B5B60", "#2C2C30"),
    soft_shadow(i, 14, 14, .4) + f'<g filter="url(#ds{i})">' + cone(i, "#F2F2F4", "#8E8E93", "#D1D1D6") + "</g>", "Minimal")
# 16 Top view
i = 16
add("Top View", "Abstract bird's-eye cone: concentric orange and white rings with a play core.",
    bg_grad(i, "#FFFFFF", "#EFEAE4"),
    soft_shadow(i, 16, 18, .25) + f'<g filter="url(#ds{i})"><rect x="232" y="232" width="560" height="560" rx="90" fill="{OR_D}"/>'
    f'<circle cx="512" cy="512" r="250" fill="{OR}"/><circle cx="512" cy="512" r="200" fill="#fff"/>'
    f'<circle cx="512" cy="512" r="150" fill="{OR}"/><circle cx="512" cy="512" r="95" fill="#fff"/>'
    f'<path d="M488,470 L560,512 L488,554 Z" fill="{OR}" stroke="{OR}" stroke-width="12" stroke-linejoin="round"/></g>', "Concept")
# 17 Realistic
i = 17
add("Studio Real", "Photo-studio realism: glossy plastic, soft floor shadow, gentle vignette.",
    bg_grad(i, "#FAFAFA", "#CFCFCF", "rg"),
    '<filter id="bl17"><feGaussianBlur stdDeviation="20"/></filter><ellipse cx="540" cy="770" rx="280" ry="36" fill="#000" opacity=".35" filter="url(#bl17)"/>'
    + cone(i, "#FF7A00", "#FAFAFA", "#E35A00", gloss=True), "3D")
# 18 Paper cut
i = 18
add("Paper Cut", "Layered paper look: stacked cut-outs with tiny shadows between layers.",
    bg_grad(i, "#FFE3C2", "#FFC98F"),
    '<filter id="pc18"><feDropShadow dx="0" dy="10" stdDeviation="8" flood-opacity=".25"/></filter>'
    f'<g filter="url(#pc18)"><circle cx="512" cy="540" r="340" fill="#FFB267"/><circle cx="512" cy="560" r="270" fill="#FF9A3D"/>'
    + cone(i, "#FF6A00", "#FFF6EC", "#E85300", shade=False) + "</g>", "Soft")
# 19 Lens
i = 19
add("Lens", "A glass lens magnifying the cone. Media optics metaphor.",
    bg_grad(i, "#FF9B2F", "#FF5800"),
    rg("ln19", "#ffffff", "#FFD7B0", .4, .35, .75) +
    f'<circle cx="512" cy="512" r="330" fill="url(#ln19)"/><circle cx="512" cy="512" r="330" fill="none" stroke="#fff" stroke-width="22" opacity=".9"/>'
    + cone(i, OR, "#fff", OR_D, cone_d=cone_path(290, 650, 150), stripes=[(410, 460), (535, 590)], base=base_shape(640, 62, 380, 22))
    + '<path d="M300,380 A240,240 0 0 1 470,230" fill="none" stroke="#fff" stroke-width="26" stroke-linecap="round" opacity=".8"/>', "Concept")
# 20 Aqua
i = 20
add("Aqua Candy", "A love letter to Mac OS X Aqua: jelly-glossy cone with a big highlight.",
    bg_grad(i, "#E8F1FB", "#B7CDE8"),
    soft_shadow(i, 20, 18, .3) + lg("aq20", "#FFB44A", "#FF5500") +
    f'<g filter="url(#ds{i})">' + cone(i, "url(#aq20)", "#fff", "#D24A00", gloss=True) +
    '<path d="M430,560 L470,330 Q478,300 490,300 L470,560 Z" fill="#fff" opacity=".6"/></g>', "Retro")
# 21 Wordmark
i = 21
add("Cone + VLC", "Cone with a clean VLC wordmark underneath — helps recognition at large sizes.",
    bg_grad(i, "#FFFFFF", "#EEE9E4"),
    cone(i, OR, "#fff", OR_D, cone_d=cone_path(220, 600, 150), stripes=[(350, 400), (475, 530)], base=base_shape(590, 60, 390, 22))
    + f'<text x="512" y="800" text-anchor="middle" font-family="Helvetica Neue,Arial,sans-serif" font-weight="800" font-size="150" letter-spacing="10" fill="#1D1D1F">VLC</text>', "Classic")
# 22 Sound waves
i = 22
add("Sound Waves", "Cone emitting audio arcs: equal weight on audio and video playback.",
    bg_grad(i, "#FFF7EF", "#FFE2C6"),
    cone(i, OR, "#fff", OR_D, cone_d=cone_path(290, 680, 150, 20), stripes=[(420, 470), (560, 610)], base=base_shape(670, 64, 400, 22)).replace('x="0"', 'x="0"') +
    '<g fill="none" stroke="#FF7A00" stroke-width="34" stroke-linecap="round">'
    '<path d="M720,380 Q770,480 720,580"/><path d="M790,320 Q870,480 790,640" opacity=".6"/>'
    '<path d="M304,380 Q254,480 304,580"/><path d="M234,320 Q154,480 234,640" opacity=".6"/></g>', "Concept")
# 23 Split tone
i = 23
add("Split Tone", "Half light, half shadow — a graphic, poster-like cone.",
    f'<rect width="1024" height="1024" fill="#FFEFE0"/><rect width="512" height="1024" fill="#FFD9B5"/>',
    cone(i, OR, "#fff", OR_D, shade=False) +
    f'<clipPath id="half23"><rect x="512" y="0" width="512" height="1024"/></clipPath>'
    f'<g clip-path="url(#half23)"><path d="{CONE}" fill="#000" opacity=".18"/><g opacity=".18">{base_shape()}</g></g>', "Bold")
# 24 Screen
i = 24
add("On Screen", "A tiny display frame with the cone inside — reads as a video player instantly.",
    bg_grad(i, "#FF9E3A", "#FF5E00"),
    soft_shadow(i, 18, 18, .3) +
    f'<g filter="url(#ds{i})"><rect x="190" y="230" width="644" height="480" rx="60" fill="#1D1D1F"/>'
    f'<rect x="222" y="262" width="580" height="416" rx="34" fill="#fff"/><rect x="430" y="720" width="164" height="50" rx="12" fill="#1D1D1F"/>'
    f'<rect x="340" y="760" width="344" height="36" rx="18" fill="#1D1D1F"/></g>'
    + cone(i, OR, "#fff", OR_D, cone_d=cone_path(300, 620, 110, 16), stripes=[(410, 445), (500, 540)], base=base_shape(612, 44, 290, 16)), "Concept")
# 25 Holographic
i = 25
add("Holo", "Iridescent holographic plate with a chrome-white cone.",
    '<linearGradient id="hb25" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFB86C"/><stop offset=".35" stop-color="#FF7EB3"/>'
    '<stop offset=".65" stop-color="#8FA8FF"/><stop offset="1" stop-color="#7DF2D0"/></linearGradient><rect width="1024" height="1024" fill="url(#hb25)"/>',
    soft_shadow(i, 20, 20, .25) + lg("ch25", "#FFFFFF", "#DAD7E6", 0, 0, 1, 1) +
    f'<g filter="url(#ds{i})">' + cone(i, "url(#ch25)", "#FF7A00", "#EDEAF4", gloss=True) + "</g>", "Bold")
# 26 Hazard
i = 26
haz = "".join(f'<path d="M{x},1024 L{x+120},1024 L{x+520},624 L{x+400},624 Z" fill="#111"/>' for x in range(-520, 1100, 240))
add("Hazard", "Brutalist black-and-orange hazard stripes, cone knocked out in white.",
    f'<rect width="1024" height="1024" fill="{OR}"/>' + f'<clipPath id="hz"><rect y="624" width="1024" height="400"/></clipPath><g clip-path="url(#hz)">{haz}</g>',
    cone(i, "#fff", "#111", "#fff", shade=False, stroke="#111", sw=18, cone_d=cone_path(170, 610, 180), stripes=[(320, 380), (460, 525)],
         base=base_shape(600, 70, 480, 20)), "Bold")
# 27 Play circle
i = 27
add("Cone Button", "The cone inside a circular play-button bezel, like a transport control.",
    bg_grad(i, "#1F1F23", "#0B0B0D"),
    rg("pb27", "#FFB04A", "#FF5A00", .4, .3, .9) +
    f'<circle cx="512" cy="512" r="330" fill="url(#pb27)"/><circle cx="512" cy="512" r="330" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="10"/>'
    + cone(i, "#fff", OR, "#FFE7D2", shade=False, cone_d=cone_path(290, 650, 150), stripes=[(410, 460), (535, 590)], base=base_shape(640, 60, 380, 22)), "Pro")
# 28 Pastel
i = 28
add("Pastel", "Peach-and-cream pastel palette: calm, friendly, very 2020s.",
    bg_grad(i, "#FFF3E6", "#FFDCC2"),
    soft_shadow(i, 14, 16, .15) + f'<g filter="url(#ds{i})">' + cone(i, "#FFA26B", "#FFF8F1", "#F3875A", shade=False) + "</g>", "Soft")
# 29 Clay
i = 29
add("Clay 3D", "Soft clay render: rounded edges, matte material, generous ambient occlusion.",
    bg_grad(i, "#B9E0FF", "#7FB6F0"),
    '<filter id="cl29" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur in="SourceAlpha" stdDeviation="18" result="b"/>'
    '<feOffset dx="-14" dy="-14" in="b" result="o1"/><feComposite in="o1" in2="SourceAlpha" operator="arithmetic" k2="-1" k3="1" result="inner"/>'
    '<feFlood flood-color="#8A2E00" flood-opacity=".45"/><feComposite in2="inner" operator="in" result="sh"/>'
    '<feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="sh"/></feMerge></filter>'
    + soft_shadow(i, 30, 26, .3) +
    f'<g filter="url(#ds{i})"><g filter="url(#cl29)">' + cone(i, "#FF8A2B", "#FFF4E8", "#F06A12", shade=False,
                                                         cone_d="M470,270 Q512,220 554,270 L690,690 Q512,720 334,690 Z") + "</g></g>", "3D")
# 30 Tahoe layered
i = 30
add("Tahoe Layered", "Guideline-true macOS 26 icon: layered foreground, specular edge light, subtle gradient plate.",
    lg("tb30", "#FFFDFB", "#F3E7DB") + '<rect width="1024" height="1024" fill="url(#tb30)"/>'
    '<ellipse cx="512" cy="760" rx="330" ry="120" fill="#FF8A00" opacity=".12"/>',
    soft_shadow(i, 22, 24, .28) + lg("tc30", "#FFA13A", "#FF5A00") +
    f'<g filter="url(#ds{i})">' + cone(i, "url(#tc30)", "#FFFFFF", "#E24E00", gloss=True) +
    f'<path d="{CONE}" fill="none" stroke="#fff" stroke-opacity=".55" stroke-width="5"/></g>', "Tahoe")

# ================= 31–50 =================
# 31 Ember glow
i = 31
add("Ember", "Dark plate with a warm ember glow rising behind a glossy cone.",
    bg_grad(i, "#2B1406", "#0C0503") + rg("eg31", "#FF7A00", "#FF7A00", .5, .5, .5).replace('stop-color="#FF7A00"/></radialGradient>', 'stop-color="#FF7A00" stop-opacity="0"/></radialGradient>')
    + '<circle cx="512" cy="600" r="420" fill="url(#eg31)" opacity=".55"/>',
    soft_shadow(i, 16, 20, .6) + f'<g filter="url(#ds{i})">' + cone(i, OR, "#FFF3E6", "#B83E00", gloss=True) + "</g>", "Dark")
# 32 Duotone
i = 32
add("Duotone", "Two-tone yellow and orange, no white at all. Warm, poster-flat and very legible.",
    f'<rect width="1024" height="1024" fill="#FFD23F"/>',
    cone(i, "#FF5E00", "#FFD23F", "#E04800", shade=False), "Bold")
# 33 Low-poly
i = 33
lp = ''.join(f'<path d="{d}" fill="{c}"/>' for d, c in [
    ("M512,236 L334,700 L470,700 Z", "#E55A00"), ("M512,236 L470,700 L560,700 Z", "#FF8A1A"),
    ("M512,236 L560,700 L690,700 Z", "#C94600"), ("M300,700 L724,700 L700,768 L324,768 Z", "#B53D00")])
add("Low Poly", "Faceted, low-polygon cone. Reads as 3D with only four flat shapes.",
    bg_grad(i, "#FFF4E8", "#FFDDBB"),
    soft_shadow(i, 18, 18, .25) + f'<g filter="url(#ds{i})">{lp}'
    '<clipPath id="lpc"><path d="M512,236 L690,700 L334,700 Z"/></clipPath><g clip-path="url(#lpc)" fill="#fff" opacity=".92">'
    '<rect y="395" width="1024" height="58"/><rect y="545" width="1024" height="64"/></g></g>', "3D")
# 34 Sticker
i = 34
add("Sticker", "Die-cut sticker with a thick white border and a slight tilt: playful, laptop-lid energy.",
    bg_grad(i, "#6C5CE7", "#3B2DB5"),
    '<filter id="st34"><feDropShadow dx="0" dy="16" stdDeviation="14" flood-opacity=".35"/></filter>'
    f'<g transform="rotate(-8 512 512)" filter="url(#st34)"><g stroke="#fff" stroke-width="60" stroke-linejoin="round" fill="#fff"><path d="{CONE}"/>{base_shape()}</g>'
    + cone(i, OR, "#fff", OR_D, shade=False) + "</g>", "Soft")
# 35 Gold
i = 35
add("Black & Gold", "Luxury edition: matte black plate, brushed-gold cone. For a Pro-tier look.",
    bg_grad(i, "#1C1C1C", "#050505"),
    lg("gd35", "#F7E08A", "#B8862B", 0, 0, 1, 1) + soft_shadow(i, 14, 18, .6) +
    f'<g filter="url(#ds{i})">' + cone(i, "url(#gd35)", "#111", "#9C7222", gloss=True) + "</g>", "Pro")
# 36 Watercolour
i = 36
add("Watercolour", "Hand-painted feel: soft pigment blooms behind a clean cone.",
    '<filter id="wc36"><feTurbulence type="fractalNoise" baseFrequency=".012" numOctaves="3" seed="4"/><feDisplacementMap in="SourceGraphic" scale="90"/><feGaussianBlur stdDeviation="10"/></filter>'
    '<rect width="1024" height="1024" fill="#FFFBF5"/><g filter="url(#wc36)" opacity=".85"><circle cx="400" cy="420" r="260" fill="#FFB36B"/><circle cx="640" cy="620" r="240" fill="#FF8FA3"/><circle cx="600" cy="360" r="170" fill="#FFD66B"/></g>',
    cone(i, "#FF6A00", "#FFFBF5", "#D94E00", shade=False), "Soft")
# 37 Stacked bars
i = 37
bars = ''.join(f'<rect x="{512-w/2}" y="{y}" width="{w}" height="84" rx="42" fill="{c}"/>' for y, w, c in
               [(250, 120, "#FFB255"), (360, 230, "#FF9433"), (470, 340, "#FF7A00"), (580, 450, "#F25F00"), (690, 560, "#D84A00")])
add("Stacked Bars", "Abstract cone built from five rounded bars, like an equaliser turned sideways.",
    bg_grad(i, "#FFFFFF", "#F1ECE6"), bars, "Minimal")
# 38 Long shadow
i = 38
add("Long Shadow", "Flat design classic: white cone casting a 45° long shadow across the plate.",
    f'<rect width="1024" height="1024" fill="{OR2}"/>',
    '<path d="M534,250 L1100,816 L1100,1100 L724,1100 L724,768 L690,700 Z" fill="#000" opacity=".16"/>'
    + cone(i, "#fff", OR2, "#fff", shade=False, stripes=[(420, 470), (560, 615)]), "Minimal")
# 39 Chrome
i = 39
add("Chrome", "Polished liquid-metal cone with an orange reflection band.",
    bg_grad(i, "#E9ECF1", "#B8BFCA"),
    '<linearGradient id="cr39" x1="0" x2="1"><stop offset="0" stop-color="#6B7280"/><stop offset=".3" stop-color="#FFFFFF"/><stop offset=".5" stop-color="#9CA3AF"/>'
    '<stop offset=".7" stop-color="#F3F4F6"/><stop offset="1" stop-color="#4B5563"/></linearGradient>' + soft_shadow(i, 20, 18, .35) +
    f'<g filter="url(#ds{i})">' + cone(i, "url(#cr39)", OR, "#6B7280", shade=False) + "</g>", "3D")
# 40 Terminal
i = 40
ascii_rows = ["    /\\", "   /  \\", "  /####\\", " /      \\", "/########\\", "==========", "$ vlc --play"]
txt = ''.join(f'<text x="200" y="{300+k*84}" font-family="Menlo,Consolas,monospace" font-size="76" font-weight="700" fill="{"#FF8A00" if k<6 else "#9BE38F"}" xml:space="preserve">{r.replace("&","&amp;")}</text>'
              for k, r in enumerate(ascii_rows))
add("Terminal", "ASCII-art cone in a terminal window, for the command-line crowd.",
    '<rect width="1024" height="1024" fill="#0F1115"/><rect width="1024" height="120" fill="#1D2026"/>'
    '<circle cx="110" cy="60" r="22" fill="#FF5F57"/><circle cx="180" cy="60" r="22" fill="#FEBC2E"/><circle cx="250" cy="60" r="22" fill="#28C840"/>',
    txt, "Retro")
# 41 Monogram V
i = 41
add("Monogram V", "The cone flipped into a V for VLC — the stripes still say 'traffic cone'.",
    bg_grad(i, "#FFA531", "#FF5B00"),
    '<clipPath id="vv"><path d="M300,270 L724,270 L540,760 Q512,790 484,760 Z"/></clipPath>'
    '<path d="M300,270 L724,270 L540,760 Q512,790 484,760 Z" fill="#fff"/><g clip-path="url(#vv)" fill="#FF6F00"><rect y="390" width="1024" height="60"/><rect y="530" width="1024" height="60"/></g>', "Concept")
# 42 Mascot
i = 42
add("Mascot", "A friendly cone character with eyes and a smile. Kid-friendly and memorable.",
    bg_grad(i, "#BDEBFF", "#7CC8F2"),
    soft_shadow(i, 20, 18, .25) + f'<g filter="url(#ds{i})">' + cone(i, OR, "#fff", OR_D, stripes=[(395, 445)]) +
    '<circle cx="470" cy="540" r="26" fill="#1D1D1F"/><circle cx="554" cy="540" r="26" fill="#1D1D1F"/><circle cx="478" cy="532" r="8" fill="#fff"/><circle cx="562" cy="532" r="8" fill="#fff"/>'
    '<path d="M470,600 Q512,640 554,600" fill="none" stroke="#1D1D1F" stroke-width="16" stroke-linecap="round"/></g>', "Soft")
# 43 Glass blobs
i = 43
add("Aurora Glass", "Dark glassmorphism: blurred aurora blobs under a frosted cone.",
    '<filter id="bl43"><feGaussianBlur stdDeviation="70"/></filter><rect width="1024" height="1024" fill="#0D0B1E"/>'
    '<g filter="url(#bl43)"><circle cx="330" cy="360" r="230" fill="#FF7A00"/><circle cx="720" cy="640" r="250" fill="#7C3AED"/><circle cx="700" cy="300" r="160" fill="#EC4899"/></g>',
    soft_shadow(i, 20, 24, .4) + f'<g filter="url(#ds{i})">' + cone(i, "rgba(255,255,255,.28)", "rgba(255,255,255,.85)", "rgba(255,255,255,.35)",
                                                              stroke="rgba(255,255,255,.8)", sw=6, gloss=True) + "</g>", "Tahoe")
# 44 Material You
i = 44
add("Material You", "Android 12+ tonal palette: soft peach container, deep-orange monochrome glyph.",
    '<rect width="1024" height="1024" fill="#FFDBC8"/>',
    cone(i, "#8B3A00", "#FFDBC8", "#8B3A00", shade=False, cone_d=cone_path(290, 670, 160), stripes=[(430, 480), (560, 612)], base=base_shape(660, 64, 420, 32)), "Minimal")
# 45 Fluent
i = 45
add("Fluent", "Windows 11 Fluent style: soft gradient cone with a subtle acrylic base, made for the taskbar.",
    bg_grad(i, "#F3F6FB", "#DDE5F0"),
    lg("fl45", "#FFB35C", "#F25A00", 0, 0, 1, 1) + lg("fb45", "#FFD9B0", "#FF9A4D", 0, 0, 1, 1) + soft_shadow(i, 12, 14, .22) +
    f'<g filter="url(#ds{i})">' + cone(i, "url(#fl45)", "#FFF6EE", "url(#fb45)", shade=False,
                                    cone_d="M478,258 Q512,226 546,258 L700,700 L324,700 Z", base=base_shape(686, 84, 500, 42)) + "</g>", "Pro")
# 46 Starfield
i = 46
import random
random.seed(46)
stars = ''.join(f'<circle cx="{random.randint(40,984)}" cy="{random.randint(40,700)}" r="{random.choice([3,4,6])}" fill="#fff" opacity="{random.choice([.4,.7,1])}"/>' for _ in range(60))
add("Night Sky", "A cone under a starry sky, with a warm glow on the horizon. Movie-night mood.",
    lg("ns46", "#0B1026", "#3A1C4A") + '<rect width="1024" height="1024" fill="url(#ns46)"/>' + stars +
    '<ellipse cx="512" cy="900" rx="700" ry="200" fill="#FF7A00" opacity=".35"/>',
    cone(i, OR, "#fff", OR_D, gloss=True), "Dark")
# 47 Wireframe
i = 47
wf = ''.join(f'<ellipse cx="512" cy="{y}" rx="{(y-236)/464*178:.0f}" ry="{(y-236)/464*44:.0f}" fill="none" stroke="#FF8A00" stroke-width="6" opacity=".9"/>' for y in range(300, 701, 50))
wf += ''.join(f'<path d="M512,236 L{512+178*math.cos(a):.0f},{700+44*math.sin(a):.0f}" stroke="#FFB870" stroke-width="5" opacity=".8"/>' for a in [k*math.pi/6 for k in range(12)])
add("Wireframe", "3D mesh wireframe of the cone, glowing on a dark grid. Engineering chic.",
    '<rect width="1024" height="1024" fill="#0B0E14"/>' + ''.join(f'<path d="M{k},0 V1024 M0,{k} H1024" stroke="#1E2633" stroke-width="3"/>' for k in range(64, 1024, 64)),
    wf + '<ellipse cx="512" cy="700" rx="178" ry="44" fill="none" stroke="#FF8A00" stroke-width="10"/>', "Concept")
# 48 Rainbow
i = 48
add("Retro Rainbow", "Six-stripe rainbow cone, a nod to 1980s Mac heritage.",
    bg_grad(i, "#FFFFFF", "#EFEFEF"),
    f'<clipPath id="rb48"><path d="{CONE}"/></clipPath><g clip-path="url(#rb48)">' +
    ''.join(f'<rect y="{240+k*78}" width="1024" height="80" fill="{c}"/>' for k, c in enumerate(["#61BB46", "#FDB827", "#F5821F", "#E03A3E", "#963D97", "#009DDC"]))
    + f'</g><g fill="#3A3A3C">{base_shape()}</g>', "Retro")
# 49 Ribbon
i = 49
add("Ribbon Play", "A single orange ribbon folds into a cone shape and a play triangle at once.",
    bg_grad(i, "#1E1E22", "#0C0C0E"),
    lg("rb49", "#FFB347", "#FF5A00", 0, 0, 1, 1) +
    '<path d="M512,220 L720,760 L304,760 Z" fill="none" stroke="url(#rb49)" stroke-width="70" stroke-linejoin="round"/>'
    '<path d="M462,470 L600,560 L462,650 Z" fill="#fff" stroke="#fff" stroke-width="24" stroke-linejoin="round"/>', "Concept")
# 50 Tahoe Dark
i = 50
add("Tahoe Dark", "Dark-mode twin of Tahoe Layered: graphite plate, same layered cone and edge light.",
    lg("td50", "#2E2E33", "#141416") + '<rect width="1024" height="1024" fill="url(#td50)"/>'
    '<ellipse cx="512" cy="760" rx="330" ry="120" fill="#FF8A00" opacity=".18"/>',
    soft_shadow(i, 22, 24, .5) + lg("tc50", "#FFA13A", "#FF5A00") +
    f'<g filter="url(#ds{i})">' + cone(i, "url(#tc50)", "#FFFFFF", "#E24E00", gloss=True) +
    f'<path d="{CONE}" fill="none" stroke="#fff" stroke-opacity=".45" stroke-width="5"/></g>', "Tahoe")
# ================= 51–100: holidays + new concepts =================
import random as _r
def star(cx, cy, r, ri=None, n=5, rot=-90, fill="#fff", op=1):
    ri = ri or r * .45
    pts = []
    for k in range(n * 2):
        a = math.radians(rot + k * 180 / n); rr = r if k % 2 == 0 else ri
        pts.append(f"{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" opacity="{op}"/>'
def heart(cx, cy, s, fill, op=1, rot=0):
    return (f'<path transform="translate({cx} {cy}) rotate({rot}) scale({s})" d="M0,30 C-60,-10 -40,-60 0,-30 C40,-60 60,-10 0,30Z" fill="{fill}" opacity="{op}"/>')
def crescent(uid, cx, cy, r, fill, dx=.38, dy=-.12):
    return (f'<mask id="cm{uid}"><rect width="1024" height="1024" fill="#fff"/><circle cx="{cx+r*dx}" cy="{cy+r*dy}" r="{r*.86}" fill="#000"/></mask>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" mask="url(#cm{uid})"/>')
def flame(cx, cy, s, fill="#FFC53D", core="#FFF3C4"):
    p = "M0,-60 C30,-25 34,6 0,26 C-34,6 -30,-25 0,-60Z"
    return (f'<g transform="translate({cx} {cy}) scale({s})"><path d="{p}" fill="{fill}"/>'
            f'<path d="{p}" fill="{core}" transform="translate(0 8) scale(.5)"/></g>')
def confetti(seed, n, colors, x0=60, x1=964, y0=60, y1=964, w=(10, 24)):
    _r.seed(seed); out = ""
    for _ in range(n):
        x, y = _r.randint(x0, x1), _r.randint(y0, y1); ww = _r.randint(*w)
        out += f'<rect x="{x}" y="{y}" width="{ww}" height="{ww*.45:.0f}" rx="3" fill="{_r.choice(colors)}" transform="rotate({_r.randint(0,180)} {x} {y})"/>'
    return out
def burst(cx, cy, r, color, n=12, sw=8):
    return ''.join(f'<path d="M{cx+r*.35*math.cos(a):.0f},{cy+r*.35*math.sin(a):.0f} L{cx+r*math.cos(a):.0f},{cy+r*math.sin(a):.0f}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>'
                   for a in [k * 2 * math.pi / n for k in range(n)]) + f'<circle cx="{cx}" cy="{cy}" r="{sw}" fill="{color}"/>'
def C(i, body=OR, stripe="#fff", basec=OR_D, s=1.0, dx=0, dy=0, **kw):
    return f'<g transform="translate({512+dx} {512+dy}) scale({s}) translate(-512 -512)">' + cone(i, body, stripe, basec, **kw) + '</g>'
def dots(seed, n, color, r=(3, 7), y1=964, op=(.4, 1)):
    _r.seed(seed)
    return ''.join(f'<circle cx="{_r.randint(40,984)}" cy="{_r.randint(40,y1)}" r="{_r.randint(*r)}" fill="{color}" opacity="{_r.uniform(*op):.2f}"/>' for _ in range(n))
def leaf(cx, cy, s, rot, fill):
    return f'<path transform="translate({cx} {cy}) rotate({rot}) scale({s})" d="M0,-40 C30,-20 30,20 0,40 C-30,20 -30,-20 0,-40Z M0,-40 L0,40" fill="{fill}" stroke="rgba(0,0,0,.18)" stroke-width="3"/>'
def flower(cx, cy, r, petal, center="#FFD23F", n=5):
    out = ''.join(f'<ellipse cx="{cx+r*.55*math.cos(a):.1f}" cy="{cy+r*.55*math.sin(a):.1f}" rx="{r*.5:.1f}" ry="{r*.36:.1f}" fill="{petal}" transform="rotate({math.degrees(a):.0f} {cx+r*.55*math.cos(a):.1f} {cy+r*.55*math.sin(a):.1f})"/>' for a in [k*2*math.pi/n for k in range(n)])
    return out + f'<circle cx="{cx}" cy="{cy}" r="{r*.3:.1f}" fill="{center}"/>'
def sh(i, dy=18, b=18, o=.3): return soft_shadow(i, dy, b, o)
def G(i, inner): return f'<g filter="url(#ds{i})">{inner}</g>'

H = []  # (name, desc, tag, bg, fg)
# ---------- 33 holidays ----------
i = 51  # Christmas
H.append(("Christmas", "Christmas · 25 Dec — a Santa-hat cone with a fur trim and pom-pom, falling snow on festive red.", "Religious",
    bg_grad(i, "#E0313F", "#8B0F1D") + dots(51, 55, "#fff", (4, 9)),
    sh(i) + G(i, cone(i, "#F2F2F2", "#E0313F", "#fff", stripes=[(395, 455), (545, 610)]) +
    '<rect x="300" y="668" width="424" height="100" rx="50" fill="#fff"/><circle cx="512" cy="232" r="46" fill="#fff"/>'
    '<g transform="translate(700 700)"><ellipse cx="-20" cy="0" rx="34" ry="16" fill="#1E7B3A" transform="rotate(-30)"/><ellipse cx="20" cy="0" rx="34" ry="16" fill="#1E7B3A" transform="rotate(30)"/><circle cx="0" cy="-6" r="12" fill="#C8102E"/></g>')))
i = 52  # Hanukkah
cand = ''.join(f'<rect x="{x-14}" y="560" width="28" height="170" rx="6" fill="#E8EEF9"/>' + flame(x, 530, .75) for x in [150, 215, 280, 345, 679, 744, 809, 874])
H.append(("Hanukkah", "Hanukkah · 8 nights in Kislev — the cone as the shamash, lighting eight candles on deep blue.", "Religious",
    bg_grad(i, "#2548B8", "#0B1B4D") + dots(52, 30, "#fff", (2, 5), 500),
    '<rect x="120" y="720" width="784" height="26" rx="13" fill="#C9D6F2"/>' + cand +
    C(i, "#FFFFFF", "#2548B8", "#C9D6F2", s=.62, dy=40, shade=False) + flame(512, 330, 1.0)))
i = 53  # New Year's Eve
H.append(("New Year's Eve", "New Year · 31 Dec — party-hat cone in gold, fireworks and confetti at midnight.", "Seasonal",
    bg_grad(i, "#1B1B3A", "#05050F") + burst(230, 250, 150, "#FFD54A") + burst(800, 220, 120, "#FF7AB6") + burst(820, 560, 90, "#7BD3FF", 10, 6)
    + confetti(53, 40, ["#FFD54A", "#FF7AB6", "#7BD3FF", "#fff"]),
    lg("ny53", "#FFE58A", "#D39B1F", 0, 0, 1, 1) + sh(i, 18, 18, .5) + G(i, cone(i, "url(#ny53)", "#1B1B3A", "#B8841A", gloss=True) + '<circle cx="512" cy="232" r="40" fill="#FFE58A"/>')))
i = 54  # Lunar New Year
lant = lambda x, y: (f'<path d="M{x},{y-150} V{y-80}" stroke="#E0B84A" stroke-width="6"/><rect x="{x-38}" y="{y-92}" width="76" height="18" rx="4" fill="#E0B84A"/>'
                     f'<ellipse cx="{x}" cy="{y}" rx="80" ry="92" fill="#E3262B"/><path d="M{x},{y-92} Q{x-60},{y} {x},{y+92} M{x},{y-92} Q{x+60},{y} {x},{y+92}" stroke="#B3121A" stroke-width="5" fill="none"/>'
                     f'<rect x="{x-38}" y="{y+86}" width="76" height="18" rx="4" fill="#E0B84A"/><path d="M{x},{y+104} V{y+170}" stroke="#E0B84A" stroke-width="10"/>')
H.append(("Lunar New Year", "Lunar New Year · Jan–Feb — red and gold cone flanked by paper lanterns.", "Seasonal",
    bg_grad(i, "#C8161D", "#7A0A0E") + '<circle cx="512" cy="540" r="330" fill="none" stroke="#E0B84A" stroke-width="10" opacity=".45"/><circle cx="512" cy="540" r="290" fill="none" stroke="#E0B84A" stroke-width="4" opacity=".35"/>',
    lant(185, 330) + lant(839, 330) + sh(i, 18, 18, .45) + G(i, C(i, "#E3262B", "#F5CE5A", "#E0B84A", s=.82, dy=40, gloss=True))))
i = 55  # Valentine's
_r.seed(55)
hearts = ''.join(heart(_r.randint(120, 900), _r.randint(120, 880), _r.uniform(.6, 1.3), _r.choice(["#fff", "#FF9CC2", "#FF4F8B"]), .8, _r.randint(-25, 25)) for _ in range(14))
H.append(("Valentine's Day", "Valentine's · 14 Feb — a candy-pink cone with heart confetti.", "Seasonal",
    bg_grad(i, "#FFB6D0", "#FF5C93") + hearts,
    sh(i, 18, 18, .25) + G(i, cone(i, "#E8175D", "#FFD1E1", "#B80F47", gloss=True) + heart(512, 505, 1.1, "#FFD1E1"))))
i = 56  # St Patrick's
sham = lambda x, y, s: f'<g transform="translate({x} {y}) scale({s})">' + heart(0, -36, 1, "#0E8A4D", 1, 0) + heart(-34, 0, 1, "#0E8A4D", 1, -90) + heart(34, 0, 1, "#0E8A4D", 1, 90) + '<path d="M0,10 Q10,60 30,80" stroke="#0E8A4D" stroke-width="10" fill="none" stroke-linecap="round"/></g>'
H.append(("St Patrick's Day", "St Patrick's · 17 Mar — Irish green, white and orange cone with a shamrock.", "National",
    bg_grad(i, "#B9F0CF", "#5CC98A") + sham(815, 240, 1.4) + sham(210, 780, 1.0),
    sh(i, 18, 18, .25) + G(i, cone(i, "#169B62", "#FFFFFF", "#FF883E"))))
i = 57  # Easter
egg = lambda x, y, s, c1, c2, rot: (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><ellipse rx="44" ry="58" fill="{c1}"/>'
                                    f'<path d="M-44,0 L-30,-10 L-15,0 L0,-10 L15,0 L30,-10 L44,0" stroke="{c2}" stroke-width="8" fill="none"/></g>')
H.append(("Easter", "Easter · Mar–Apr — a hand-painted egg-pattern cone, pastel eggs at its base.", "Religious",
    bg_grad(i, "#E3F7EE", "#BDE8F5"),
    sh(i, 16, 16, .2) + G(i, cone(i, "#FFB27A", "#FFF", "#F38A4E", shade=False) +
    '<clipPath id="ez57"><path d="' + CONE + '"/></clipPath><g clip-path="url(#ez57)"><path d="M300,490 L360,470 L420,490 L480,470 L540,490 L600,470 L660,490 L720,470" stroke="#9AD7F0" stroke-width="16" fill="none"/></g>'
    + egg(250, 740, 1, "#FFD1E8", "#fff", -15) + egg(780, 745, 1.05, "#C9F2D4", "#fff", 12) + egg(170, 700, .75, "#FFF1A8", "#fff", -25))))
i = 58  # Ramadan
fanous = (f'<g transform="translate(250 330)"><path d="M0,-200 V-120" stroke="#E6C36A" stroke-width="6"/><path d="M-30,-120 H30 L20,-90 H-20Z" fill="#E6C36A"/>'
          f'<path d="M-50,-90 H50 L40,60 H-40Z" fill="#E6C36A"/><path d="M-36,-78 H36 L28,48 H-28Z" fill="#FFC857" opacity=".95"/>'
          f'<path d="M0,-78 V48 M-32,-15 H32" stroke="#B8923A" stroke-width="5"/><path d="M-40,60 H40 L0,110Z" fill="#E6C36A"/></g>')
H.append(("Ramadan", "Ramadan · 9th month — a glowing fanous lantern and crescent over a calm night.", "Religious",
    bg_grad(i, "#1E2A5A", "#0A0F2A") + dots(58, 40, "#fff", (2, 5), 600) + crescent(i, 780, 230, 110, "#F6D77A"),
    fanous + sh(i, 18, 18, .5) + G(i, C(i, OR, "#F6D77A", "#C9702A", s=.78, dx=90, dy=60, gloss=True))))
i = 59  # Eid al-Fitr
tile = ''.join(star(x, y, 34, 24, 8, -90, "#E6C36A", .35) for x in range(64, 1024, 128) for y in range(64, 1024, 128))
H.append(("Eid al-Fitr", "Eid al-Fitr · end of Ramadan — emerald and gold, geometric stars and a festive crescent.", "Religious",
    bg_grad(i, "#0F7A54", "#064431") + tile + crescent(i, 790, 230, 100, "#F2D27A"),
    sh(i, 18, 18, .45) + G(i, cone(i, "#F7F2E4", "#0F7A54", "#E6C36A", gloss=True))))
i = 60  # Eid al-Adha
arch = "M232,900 V430 Q232,200 512,150 Q792,200 792,430 V900 Z"
H.append(("Eid al-Adha", "Eid al-Adha · 10 Dhu al-Hijjah — the cone framed in a warm, pointed arch with a crescent.", "Religious",
    bg_grad(i, "#F5E1B8", "#D9A95B"),
    f'<path d="{arch}" fill="#FFF8EA"/><path d="{arch}" fill="none" stroke="#B9822F" stroke-width="18"/>' + crescent(i, 512, 270, 44, "#B9822F", .4, -.2)
    + sh(i, 14, 14, .25) + G(i, C(i, OR, "#fff", OR_D, s=.72, dy=90))))
i = 61  # Diwali
diya = lambda x, y: f'<path d="M{x-58},{y} Q{x},{y+70} {x+58},{y} Z" fill="#C8561C"/><path d="M{x-58},{y} H{x+58}" stroke="#F2A541" stroke-width="8"/>' + flame(x, y - 30, .7)
rang = ''.join(f'<ellipse cx="512" cy="330" rx="40" ry="130" fill="{c}" transform="rotate({k*30} 512 470)" opacity=".85"/>' for k, c in enumerate(["#FF4F8B", "#FFC53D", "#2EC4B6", "#9B5DE5"] * 3))
H.append(("Diwali", "Diwali · Oct–Nov — a rangoli bloom, clay diyas and a cone lit like a lamp.", "Religious",
    bg_grad(i, "#4A1257", "#1C0622") + rang + '<circle cx="512" cy="470" r="120" fill="#4A1257"/>',
    ''.join(diya(x, 840) for x in [150, 330, 694, 874]) + sh(i, 16, 16, .5) + G(i, C(i, OR, "#FFE08A", "#C8561C", s=.72, dy=10, gloss=True)) + flame(512, 190, .9)))
i = 62  # Holi
H.append(("Holi", "Holi · Phalguna full moon — bursts of coloured powder and a paint-splashed cone.", "Religious",
    '<filter id="hb62"><feGaussianBlur stdDeviation="45"/></filter><rect width="1024" height="1024" fill="#FFFDF7"/><g filter="url(#hb62)">'
    '<circle cx="230" cy="250" r="190" fill="#FF3DA5"/><circle cx="800" cy="260" r="180" fill="#FFC300"/><circle cx="220" cy="800" r="190" fill="#00C2A8"/><circle cx="810" cy="790" r="190" fill="#7B4DFF"/></g>',
    sh(i, 16, 16, .2) + G(i, cone(i, OR, "#FF3DA5", "#7B4DFF", stripes=[(395, 455), (545, 610)]) + '<circle cx="450" cy="600" r="22" fill="#00C2A8"/><circle cx="590" cy="440" r="18" fill="#FFC300"/><circle cx="560" cy="660" r="14" fill="#fff"/>')))
i = 63  # Navratri
nine = ["#E53935", "#1E88E5", "#FDD835", "#43A047", "#9E9E9E", "#FB8C00", "#FFFFFF", "#EC407A", "#6A1B9A"]
H.append(("Navratri", "Navratri · nine nights — the nine day-colours as rays behind a white cone.", "Religious",
    '<rect width="1024" height="1024" fill="#1A1033"/>' + ''.join(f'<path d="M512,760 L{512+900*math.cos(math.radians(200+k*15.5)):.0f},{760+900*math.sin(math.radians(200+k*15.5)):.0f} L{512+900*math.cos(math.radians(213+k*15.5)):.0f},{760+900*math.sin(math.radians(213+k*15.5)):.0f}Z" fill="{c}"/>' for k, c in enumerate(nine)),
    sh(i, 18, 18, .45) + G(i, cone(i, "#FFFFFF", "#E53935", "#FDD835"))))
i = 64  # Rosh Hashanah
H.append(("Rosh Hashanah", "Rosh Hashanah · Tishrei — a sweet new year: apple, honey drop and honey-gold stripes.", "Religious",
    bg_grad(i, "#FFF6E0", "#FFE0A3"),
    '<circle cx="780" cy="720" r="95" fill="#D7263D"/><circle cx="740" cy="690" r="28" fill="#fff" opacity=".35"/><path d="M780,625 Q790,590 815,580" stroke="#6B3E1F" stroke-width="12" fill="none" stroke-linecap="round"/><ellipse cx="835" cy="600" rx="30" ry="14" fill="#3E9B4F" transform="rotate(-20 835 600)"/>'
    '<path d="M235,240 C265,300 280,330 280,355 A45,45 0 0 1 190,355 C190,330 205,300 235,240Z" fill="#F4A300"/>'
    + sh(i, 16, 16, .22) + G(i, C(i, OR, "#FFD36B", OR_D, s=.85, dx=-40))))
i = 65  # Vesak
lotus = ''.join(f'<ellipse cx="512" cy="700" rx="50" ry="130" fill="{c}" transform="rotate({a} 512 780)"/>' for a, c in [(-60, "#F7B4D2"), (60, "#F7B4D2"), (-30, "#F59AC3"), (30, "#F59AC3"), (0, "#F287B7")])
H.append(("Vesak", "Vesak · full moon of Vesākha — the cone rising from a lotus under soft lanterns.", "Religious",
    bg_grad(i, "#3B2E7A", "#141033") + '<circle cx="512" cy="360" r="300" fill="#FFE9A8" opacity=".12"/>' + dots(65, 18, "#FFD27A", (8, 14), 420),
    lotus + sh(i, 16, 16, .4) + G(i, C(i, OR, "#FFF3D6", OR_D, s=.66, dy=-40, gloss=True))))
i = 66  # Halloween
bat = lambda x, y, s: f'<path transform="translate({x} {y}) scale({s})" d="M0,0 Q-20,-20 -40,-10 Q-50,-30 -80,-20 Q-60,0 -70,20 Q-40,10 -20,20 Q-10,10 0,20 Q10,10 20,20 Q40,10 70,20 Q60,0 80,-20 Q50,-30 40,-10 Q20,-20 0,0Z" fill="#120A1F"/>'
H.append(("Halloween", "Halloween · 31 Oct — the cone becomes a witch's hat under a harvest moon.", "Seasonal",
    bg_grad(i, "#5B2A86", "#1A0B2E") + '<circle cx="740" cy="280" r="150" fill="#FFB347"/>' + bat(300, 250, 1.3) + bat(820, 520, .9) + bat(200, 480, .8),
    sh(i, 18, 18, .5) + G(i, '<ellipse cx="512" cy="720" rx="300" ry="54" fill="#1B1025"/>' +
    cone(i, "#241536", OR, "#241536", stripes=[(590, 640)], base='<rect x="0" y="0" width="0" height="0"/>', cone_d="M470,250 Q520,200 560,280 L690,700 L334,700 Z") +
    '<rect x="470" y="585" width="84" height="62" rx="8" fill="none" stroke="#FFD27A" stroke-width="10"/>')))
i = 67  # Día de los Muertos
pic = ''.join(f'<path d="M{x},60 H{x+128} V170 L{x+96},150 L{x+64},170 L{x+32},150 L{x},170Z" fill="{c}"/>' for x, c in zip(range(0, 1024, 128), ["#FF4F8B", "#FFC53D", "#2EC4B6", "#9B5DE5"] * 2))
H.append(("Día de los Muertos", "Día de Muertos · 1–2 Nov — papel picado, marigolds and a joyful magenta plate.", "National",
    bg_grad(i, "#D6247A", "#7E0E4A") + '<path d="M0,60 H1024" stroke="#fff" stroke-width="4"/>' + pic,
    ''.join(flower(x, y, 64, "#FF9F1C", "#E65100", 10) for x, y in [(190, 780), (840, 790), (150, 560), (880, 560)]) + sh(i, 18, 18, .4) + G(i, C(i, OR, "#fff", OR_D, s=.85, dy=40))))
i = 68  # Thanksgiving
_r.seed(68)
lvs = ''.join(leaf(_r.randint(100, 920), _r.randint(100, 900), _r.uniform(1, 1.8), _r.randint(0, 360), _r.choice(["#C0392B", "#E67E22", "#F1C40F", "#8E4B1F"])) for _ in range(16))
H.append(("Thanksgiving", "Thanksgiving · Nov — warm autumn plate with falling leaves around the cone.", "National",
    bg_grad(i, "#F6D7A7", "#D98B3A") + lvs,
    sh(i, 18, 18, .3) + G(i, cone(i, "#E0621B", "#FFF3E0", "#8E4B1F"))))
i = 69  # July 4th
H.append(("Independence Day (US)", "Fourth of July · 4 Jul — stars and stripes cone with fireworks over navy.", "National",
    bg_grad(i, "#1F3A93", "#0A1640") + burst(220, 240, 140, "#fff") + burst(810, 250, 130, "#E23B3B") + ''.join(star(x, y, 18, 8, 5, -90, "#fff", .6) for x, y in [(160, 600), (880, 620), (820, 850), (200, 860), (512, 150)]),
    sh(i, 18, 18, .5) + G(i, cone(i, "#E23B3B", "#FFFFFF", "#1F3A93", stripes=[(330, 380), (440, 490), (550, 600)]) + ''.join(star(x, 730, 16, 7, 5, -90, "#fff") for x in range(360, 680, 60)))))
i = 70  # Bastille Day
H.append(("Fête nationale (FR)", "14 Juillet — bleu, blanc, rouge: a tricolore plate with a white cone and fireworks.", "National",
    '<rect width="341" height="1024" fill="#1F3FAE"/><rect x="341" width="342" height="1024" fill="#FFFFFF"/><rect x="683" width="341" height="1024" fill="#E1242E"/>' + burst(170, 220, 110, "#FFD54A", 12, 7) + burst(854, 230, 110, "#FFD54A", 12, 7),
    sh(i, 18, 18, .3) + G(i, cone(i, "#F4F4F4", "#1F3FAE", "#E1242E", stripes=[(395, 455), (545, 610)]))))
i = 71  # Oktoberfest
loz = ''.join(f'<path d="M{x},{y-60} L{x+45},{y} L{x},{y+60} L{x-45},{y}Z" fill="#2F7DE1"/>' for x in range(0, 1100, 90) for y in range(0, 1100, 120)) + \
      ''.join(f'<path d="M{x+45},{y} L{x+90},{y+60} L{x+45},{y+120} L{x},{y+60}Z" fill="#2F7DE1"/>' for x in range(0, 1100, 90) for y in range(0, 1100, 120))
pretzel = '<g transform="translate(790 790)" fill="none" stroke="#8B4A1C" stroke-width="26" stroke-linecap="round"><path d="M-70,40 C-110,-30 -60,-90 0,-30 C60,-90 110,-30 70,40 M-70,40 L40,-40 M70,40 L-40,-40"/></g>'
H.append(("Oktoberfest", "Oktoberfest · Sep–Oct, Munich — Bavarian lozenges, a pretzel and a blue-striped cone.", "National",
    '<rect width="1024" height="1024" fill="#FFFFFF"/>' + loz, sh(i, 18, 18, .35) + G(i, C(i, OR, "#FFFFFF", "#2A5DB0", s=.9, dy=-20, stripe_c=None) if False else cone(i, OR, "#fff", "#2A5DB0")) + pretzel))
i = 72  # Carnival
feather = lambda rot, c: f'<ellipse cx="512" cy="330" rx="60" ry="220" fill="{c}" transform="rotate({rot} 512 620)" opacity=".9"/>'
H.append(("Carnaval (Rio)", "Carnival · before Lent — a feathered cone in green, yellow and blue with confetti.", "National",
    bg_grad(i, "#00A859", "#006B3A") + ''.join(feather(r, c) for r, c in [(-50, "#FFDF00"), (-25, "#3E4095"), (0, "#FFDF00"), (25, "#3E4095"), (50, "#FFDF00")]) + confetti(72, 50, ["#FFDF00", "#fff", "#FF4F8B", "#3E4095"]),
    sh(i, 18, 18, .4) + G(i, C(i, OR, "#FFDF00", OR_D, s=.8, dy=80, gloss=True))))
i = 73  # Pride
pr = ["#E40303", "#FF8C00", "#FFED00", "#008026", "#004DFF", "#750787"]
chev = [("#FFFFFF", 0), ("#FFAFC8", 60), ("#74D7EE", 120), ("#613915", 180), ("#000000", 240)]
H.append(("Pride", "Pride Month · June — Progress-flag plate with a clean white cone.", "Seasonal",
    ''.join(f'<rect y="{k*171}" width="1024" height="172" fill="{c}"/>' for k, c in enumerate(pr)) + ''.join(f'<path d="M{-300+o},0 L{212+o},512 L{-300+o},1024 L{-420+o},1024 L{92+o},512 L{-420+o},0Z" fill="{c}"/>' for c, o in chev[::-1]),
    sh(i, 18, 18, .35) + G(i, C(i, "#FFFFFF", "#F2F2F2", "#FFFFFF", s=.86, dx=90, shade=True))))
i = 74  # King's Day
crown = '<g transform="translate(512 215)"><path d="M-110,40 L-120,-60 L-60,-10 L0,-80 L60,-10 L120,-60 L110,40Z" fill="#F7C948" stroke="#C99A1E" stroke-width="8" stroke-linejoin="round"/><circle cx="0" cy="-80" r="14" fill="#E1242E"/><circle cx="-120" cy="-60" r="12" fill="#1F3FAE"/><circle cx="120" cy="-60" r="12" fill="#1F3FAE"/></g>'
H.append(("King's Day (NL)", "Koningsdag · 27 Apr — the Netherlands goes orange; the cone finally gets its crown.", "National",
    bg_grad(i, "#FF9A1F", "#FF5E00"), sh(i, 18, 18, .3) + G(i, C(i, "#FFFFFF", "#FF6F00", "#F1ECE6", s=.86, dy=60, shade=False) + crown)))
i = 75  # Canada Day
H.append(("Canada Day", "Canada Day · 1 Jul — the flag's layout, with the cone standing in for the maple leaf.", "National",
    '<rect width="1024" height="1024" fill="#fff"/><rect width="256" height="1024" fill="#D52B1E"/><rect x="768" width="256" height="1024" fill="#D52B1E"/>',
    C(i, "#D52B1E", "#FFFFFF", "#A51F15", s=.78, shade=False)))
i = 76  # Bonfire Night
fire = ''.join(f'<path transform="translate({x} 860) scale({s})" d="M0,-160 C60,-90 70,-20 0,20 C-70,-20 -60,-90 0,-160Z" fill="{c}"/>' for x, s, c in [(420, 1.1, "#FF5A00"), (600, 1.2, "#FF5A00"), (512, 1.5, "#FF8A00"), (512, .9, "#FFD54A")])
H.append(("Bonfire Night (UK)", "Guy Fawkes Night · 5 Nov — sparkler trails and a bonfire glow.", "National",
    bg_grad(i, "#1A1030", "#060310") + burst(220, 230, 130, "#FFD54A") + burst(820, 280, 100, "#8FE3FF", 10, 6) + '<ellipse cx="512" cy="900" rx="520" ry="160" fill="#FF6A00" opacity=".35"/>' + fire,
    sh(i, 18, 18, .5) + G(i, C(i, OR, "#fff", OR_D, s=.72, dy=-40, gloss=True))))
i = 77  # Songkran
drops = ''.join(f'<path transform="translate({x} {y}) scale({s})" d="M0,-40 C20,-10 26,10 0,26 C-26,10 -20,-10 0,-40Z" fill="#fff" opacity=".85"/>' for x, y, s in [(200, 260, 1.2), (820, 220, 1), (870, 600, 1.3), (160, 640, .9), (700, 120, .7), (300, 880, .8)])
H.append(("Songkran", "Songkran · 13–15 Apr, Thai New Year — water-splash turquoise and a freshly rinsed cone.", "National",
    bg_grad(i, "#3DD6E0", "#0E88B5") + '<path d="M0,760 Q256,690 512,760 T1024,760 V1024 H0Z" fill="#fff" opacity=".25"/>' + drops,
    sh(i, 18, 18, .3) + G(i, cone(i, OR, "#E6FBFF", OR_D, gloss=True))))
i = 78  # Nowruz
_r.seed(78)
grass = ''.join(f'<path d="M{x},790 Q{x+_r.randint(-20,20)},{720-_r.randint(0,40)} {x+_r.randint(-30,30)},{660-_r.randint(0,60)}" stroke="{_r.choice(["#5BBF3A", "#3E9B2A", "#7ED957"])}" stroke-width="10" fill="none" stroke-linecap="round"/>' for x in range(250, 780, 16))
H.append(("Nowruz", "Nowruz · 20–21 Mar, Persian New Year — spring sabzeh sprouting around the cone.", "National",
    bg_grad(i, "#E8F8D8", "#A7DDB0") + ''.join(flower(x, y, 40, "#FF9EC4", "#FFE066") for x, y in [(180, 220), (860, 260), (820, 480)]),
    grass + '<rect x="230" y="780" width="564" height="80" rx="40" fill="#C9A26B"/>' + sh(i, 14, 14, .25) + G(i, C(i, OR, "#fff", OR_D, s=.66, dy=-70))))
i = 79  # Hanami
H.append(("Hanami", "Hanami · cherry-blossom season, Japan — pale pink petals drifting past a pink-striped cone.", "Seasonal",
    bg_grad(i, "#FFF0F5", "#FFC9DC") + ''.join(flower(x, y, s, "#FF9EC4", "#E0457B") for x, y, s in [(170, 200, 70), (860, 190, 60), (880, 520, 50), (150, 560, 46), (280, 860, 40), (790, 850, 56)]),
    sh(i, 16, 16, .2) + G(i, cone(i, OR, "#FFD6E6", OR_D))))
i = 80  # Santo António (Lisbon)
az = ''.join(f'<g transform="translate({x} {y})"><rect width="128" height="128" fill="#F4F7FC"/><path d="M64,10 L118,64 L64,118 L10,64Z" fill="none" stroke="#1D4E9E" stroke-width="8"/><circle cx="64" cy="64" r="18" fill="#1D4E9E"/><path d="M0,0 L24,0 L0,24Z M128,0 L104,0 L128,24Z M0,128 L24,128 L0,104Z M128,128 L104,128 L128,104Z" fill="#1D4E9E"/></g>' for x in range(0, 1024, 128) for y in range(0, 1024, 128))
sard = '<g transform="translate(800 820) rotate(-20)"><ellipse rx="110" ry="34" fill="#9FB3C8"/><path d="M100,0 L160,-40 L160,40Z" fill="#9FB3C8"/><circle cx="-70" cy="-6" r="7" fill="#1D2B3A"/><path d="M-40,-20 Q0,-30 60,-18" stroke="#6E8399" stroke-width="5" fill="none"/></g>'
H.append(("Santo António (Lisboa)", "Santos Populares · 13 Jun, Lisbon — azulejo tiles, a grilled sardine and a festive cone.", "National",
    az, sh(i, 18, 18, .35) + G(i, cone(i, OR, "#fff", OR_D)) + sard))
i = 81  # Earth Day
H.append(("Earth Day", "Earth Day · 22 Apr — the cone standing on a small green-and-blue planet.", "Seasonal",
    bg_grad(i, "#DFF6FF", "#9DDCF5"),
    '<circle cx="512" cy="1080" r="480" fill="#2E86DE"/><path d="M160,760 Q260,650 380,700 Q450,730 430,800 Q400,860 300,860Z M620,690 Q760,640 860,740 Q800,800 700,780 Q640,760 620,690Z" fill="#3FBF6F"/>'
    + sh(i, 14, 14, .25) + G(i, C(i, OR, "#fff", OR_D, s=.72, dy=-60)) + leaf(790, 250, 1.6, 30, "#3FBF6F") + leaf(230, 300, 1.3, -40, "#56D17E")))
i = 82  # Mid-Autumn
H.append(("Mid-Autumn Festival", "Mid-Autumn · 15th of the 8th lunar month — full moon, lantern and mooncake pattern.", "Seasonal",
    bg_grad(i, "#16244F", "#070D22") + '<circle cx="512" cy="430" r="330" fill="#FFE39A"/><circle cx="512" cy="430" r="330" fill="none" stroke="#F2C35E" stroke-width="10" stroke-dasharray="40 18"/>' + dots(82, 30, "#fff", (2, 4), 1000, (.3, .8)),
    lant(170, 420) + sh(i, 16, 16, .45) + G(i, C(i, OR, "#FFF2CC", OR_D, s=.8, dy=40, gloss=True))))
i = 83  # Midsummer
crownf = ''.join(flower(512 + 170 * math.cos(a), 700 + 50 * math.sin(a), 38, c, "#FFE066") for a, c in zip([k * 2 * math.pi / 9 for k in range(9)], ["#fff", "#8FB8FF", "#FFD23F", "#FF9EC4"] * 3))
H.append(("Midsummer", "Midsummer · late June, Nordics — midnight-sun sky and a flower crown around the cone.", "Seasonal",
    lg("ms83", "#7EC8FF", "#FFE6A8") + '<rect width="1024" height="1024" fill="url(#ms83)"/><rect y="820" width="1024" height="204" fill="#6FBF5A"/>',
    sh(i, 16, 16, .25) + G(i, cone(i, OR, "#fff", OR_D)) + '<ellipse cx="512" cy="700" rx="170" ry="50" fill="none" stroke="#3E9B2A" stroke-width="12"/>' + crownf))

# ---------- 17 new concepts ----------
i = 84
H.append(("Outline Plate", "Stroke-only plate and cone in brand orange on near-black. Quiet, crisp, very Pro.", "Minimal",
    '<rect width="1024" height="1024" fill="#111113"/>' + f'<path d="{squircle(512,512,420)}" fill="none" stroke="#FF7A00" stroke-width="18"/>',
    f'<g fill="none" stroke="#FF7A00" stroke-width="30" stroke-linejoin="round" stroke-linecap="round"><path d="{cone_path(290, 680, 160)}"/><path d="M320,720 H704"/><path d="M440,450 H584"/><path d="M405,570 H619"/></g>'))
i = 85
H.append(("Glitch", "RGB-split glitch cone with scanlines, for a VHS-era vibe.", "Retro",
    '<rect width="1024" height="1024" fill="#0A0A0C"/>' + ''.join(f'<rect y="{y}" width="1024" height="3" fill="#fff" opacity=".05"/>' for y in range(0, 1024, 12)),
    f'<g style="mix-blend-mode:screen"><g transform="translate(-22 0)">{cone(851, "#00E5FF", "#0A0A0C", "#00E5FF", shade=False)}</g><g transform="translate(22 0)">{cone(852, "#FF2BD6", "#0A0A0C", "#FF2BD6", shade=False)}</g></g>'
    + cone(i, "#FFFFFF", "#0A0A0C", "#FFFFFF", shade=False) + '<rect x="300" y="500" width="440" height="20" fill="#0A0A0C"/><rect x="340" y="505" width="200" height="10" fill="#00E5FF"/>'))
i = 86
H.append(("Vaporwave", "Synthwave sunset with a neon grid floor: the cone as a retro-future monument.", "Retro",
    lg("vw86", "#2B0B5A", "#FF3CAC") + '<rect width="1024" height="1024" fill="url(#vw86)"/>' + lg("sn86", "#FFE259", "#FF3CAC") + '<circle cx="512" cy="520" r="280" fill="url(#sn86)"/>' +
    ''.join(f'<rect y="{y}" width="1024" height="{h}" fill="#5A1A8A"/>' for y, h in [(560, 14), (610, 18), (660, 22)]) + '<rect y="700" width="1024" height="324" fill="#1A0535"/>' +
    ''.join(f'<path d="M512,700 L{x},1024" stroke="#FF3CAC" stroke-width="4"/>' for x in range(-600, 1700, 160)) + ''.join(f'<path d="M0,{y} H1024" stroke="#FF3CAC" stroke-width="4"/>' for y in [730, 780, 850, 950]),
    C(i, "#1A0535", "#FF3CAC", "#FF3CAC", s=.78, dy=40, shade=False, stroke="#00F0FF", sw=10)))
i = 87
H.append(("Marble", "White Carrara marble plate with gold veining under a gilded cone.", "Pro",
    '<filter id="mb87"><feTurbulence type="fractalNoise" baseFrequency=".008 .02" numOctaves="4" seed="9"/><feColorMatrix values="0 0 0 0 .55  0 0 0 0 .55  0 0 0 0 .58  0 0 0 -2.2 1.35"/></filter>'
    '<rect width="1024" height="1024" fill="#F7F5F2"/><rect width="1024" height="1024" filter="url(#mb87)" opacity=".7"/>',
    lg("mg87", "#F9E3A1", "#B98A2E", 0, 0, 1, 1) + sh(i, 16, 16, .3) + G(i, cone(i, "url(#mg87)", "#FFFFFF", "#9A7224", gloss=True))))
i = 88
H.append(("Embroidered Patch", "A stitched round patch with a twill texture — the jacket-sleeve version of VLC.", "Soft",
    '<rect width="1024" height="1024" fill="#2B3A55"/>',
    '<circle cx="512" cy="512" r="370" fill="#FF7A00"/><circle cx="512" cy="512" r="370" fill="none" stroke="#FFD2A6" stroke-width="30"/><circle cx="512" cy="512" r="330" fill="none" stroke="#fff" stroke-width="6" stroke-dasharray="18 12"/>'
    + ''.join(f'<path d="M{x},150 L{x-300},870" stroke="#000" stroke-opacity=".05" stroke-width="6"/>' for x in range(300, 1200, 22))
    + C(i, "#FFFFFF", "#FF7A00", "#FFFFFF", s=.72, shade=False, stroke="#E55A00", sw=6)))
i = 89
def cube(x, y, s, top, left, right):
    return (f'<path d="M{x},{y} L{x+s},{y-s*.5} L{x+2*s},{y} L{x+s},{y+s*.5}Z" fill="{top}"/>'
            f'<path d="M{x},{y} L{x+s},{y+s*.5} L{x+s},{y+s*1.5} L{x},{y+s}Z" fill="{left}"/>'
            f'<path d="M{x+s},{y+s*.5} L{x+2*s},{y} L{x+2*s},{y+s} L{x+s},{y+s*1.5}Z" fill="{right}"/>')
vox = ''
for lvl, (n, col) in enumerate([(4, "o"), (3, "w"), (3, "o"), (2, "w"), (1, "o")]):
    s = 64; y = 690 - lvl * 92
    c = ("#FFA64D", "#FF7A00", "#C85200") if col == "o" else ("#FFFFFF", "#E6E6E6", "#BDBDBD")
    for k in range(n):
        vox += cube(512 - n * s + k * 2 * s, y, s, *c)
H.append(("Voxel", "Isometric voxel cone stacked from orange and white blocks. Very Minecraft, very readable.", "3D",
    bg_grad(i, "#EAF2FF", "#BFD3F2"), '<ellipse cx="512" cy="860" rx="260" ry="50" fill="#000" opacity=".12"/>' + vox))
i = 90
H.append(("Spotlight", "A theatre spotlight beam lands on the cone. Showtime.", "Dark",
    '<rect width="1024" height="1024" fill="#0B0B0E"/>' + lg("sp90", "#FFF6D6", "#FFF6D6") .replace('stop-color="#FFF6D6"/></linearGradient>', 'stop-color="#FFF6D6" stop-opacity="0"/></linearGradient>')
    + '<path d="M430,0 H594 L860,800 H164Z" fill="url(#sp90)" opacity=".35"/><ellipse cx="512" cy="780" rx="340" ry="70" fill="#FFF6D6" opacity=".25"/>',
    sh(i, 16, 16, .6) + G(i, cone(i, OR, "#fff", OR_D, gloss=True))))
i = 91
H.append(("Origami", "Folded paper cone: two crisp planes and a paper-white base.", "Soft",
    bg_grad(i, "#F2EFEA", "#DCD6CC"),
    '<filter id="og91"><feDropShadow dx="0" dy="14" stdDeviation="12" flood-opacity=".22"/></filter><g filter="url(#og91)">'
    '<path d="M512,220 L512,720 L320,720Z" fill="#FF8A1F"/><path d="M512,220 L704,720 L512,720Z" fill="#E0600A"/>'
    '<path d="M512,420 L570,570 L454,570Z" fill="#FFF" opacity=".92"/><path d="M512,420 L570,570 L512,570Z" fill="#E9E4DC"/>'
    '<path d="M290,720 H734 L700,790 H324Z" fill="#FAF8F5"/></g>'))
i = 92
H.append(("Stencil", "Street-art stencil sprayed on a brick wall, with overspray speckle.", "Bold",
    '<rect width="1024" height="1024" fill="#8E3B2A"/>' + ''.join(f'<rect x="{(x + (y//64)%2*64)}" y="{y}" width="124" height="58" rx="4" fill="#A5503C"/>' for x in range(-64, 1024, 128) for y in range(0, 1024, 64)),
    '<filter id="spr92"><feTurbulence baseFrequency=".9" numOctaves="1" seed="3"/><feDisplacementMap in="SourceGraphic" scale="14"/></filter>'
    '<g filter="url(#spr92)">' + cone(i, "#FF8A00", "#8E3B2A", "#FF8A00", shade=False) + '</g>' + dots(92, 80, "#FF8A00", (2, 4), 1000, (.3, .7))))
i = 93
H.append(("Halftone Pop", "Pop-art comic cone: black ink outlines on a halftone yellow burst.", "Bold",
    '<rect width="1024" height="1024" fill="#FFE14D"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="{5 + (x+y)%1024/90:.1f}" fill="#FF6A3D" opacity=".55"/>' for x in range(0, 1040, 40) for y in range(0, 1040, 40)),
    cone(i, "#FF7A00", "#FFFFFF", "#FF5500", shade=False, stroke="#111", sw=22)))
i = 94
drip = "M334,700 L690,700 L690,760 Q690,800 670,800 Q650,800 650,760 L650,740 Q640,860 610,860 Q580,860 580,780 L560,740 Q550,900 520,900 Q490,900 490,780 L460,740 Q450,820 420,820 Q395,820 395,760 L380,740 Q370,790 350,790 Q334,790 334,760Z"
H.append(("Melt", "The cone melting like an ice-lolly on a hot day. Surreal, very memorable.", "Concept",
    bg_grad(i, "#FFF1D6", "#FFD39A"),
    f'<path d="{drip}" fill="{OR_D}"/>' + cone(i, OR, "#fff", OR_D, base='<rect x="0" y="0" width="0" height="0"/>') + '<ellipse cx="520" cy="930" rx="90" ry="18" fill="#E35A00" opacity=".6"/>'))
i = 95
pts = [(512, 240), (440, 430), (584, 430), (400, 560), (624, 560), (350, 700), (512, 700), (674, 700)]
lines = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 7), (5, 6), (6, 7)]
H.append(("Constellation", "The cone drawn as a star constellation over deep navy.", "Dark",
    bg_grad(i, "#101B3F", "#050A1C") + dots(95, 70, "#fff", (1, 3), 1000, (.2, .7)),
    ''.join(f'<path d="M{pts[a][0]},{pts[a][1]} L{pts[b][0]},{pts[b][1]}" stroke="#FFB870" stroke-width="5" opacity=".7"/>' for a, b in lines)
    + ''.join(f'<circle cx="{x}" cy="{y}" r="16" fill="#FFD9A8"/><circle cx="{x}" cy="{y}" r="34" fill="#FF8A00" opacity=".25"/>' for x, y in pts)))
i = 96
H.append(("Tangram", "Seven tangram pieces arranged into a cone. Puzzle-box charm.", "Concept",
    bg_grad(i, "#F7F4EE", "#E6DFD2"),
    '<g stroke="#F7F4EE" stroke-width="10" stroke-linejoin="round">'
    '<path d="M512,230 L600,460 L424,460Z" fill="#FF8A00"/><path d="M424,460 L600,460 L512,560Z" fill="#FFFFFF"/><path d="M424,460 L512,560 L380,580Z" fill="#E0600A"/>'
    '<path d="M600,460 L644,580 L512,560Z" fill="#FFB25C"/><path d="M380,580 L644,580 L690,700 L334,700Z" fill="#FF7A00"/>'
    '<path d="M300,700 H512 L512,770 H320Z" fill="#C24A00"/><path d="M512,700 H724 L704,770 H512Z" fill="#8F3600"/></g>'))
i = 97
H.append(("Negative Space", "An orange disc with the cone cut clean out of it. Pure figure-ground.", "Minimal",
    '<rect width="1024" height="1024" fill="#FFFFFF"/>',
    f'<mask id="ns97"><rect width="1024" height="1024" fill="#fff"/><g fill="#000"><path d="{cone_path(250, 690, 170)}"/><rect x="300" y="700" width="424" height="50" rx="20"/></g>'
    '<g fill="#fff"><rect x="0" y="420" width="1024" height="50"/><rect x="0" y="560" width="1024" height="50"/></g></mask>'
    '<circle cx="512" cy="512" r="380" fill="#FF7A00" mask="url(#ns97)"/>'))
i = 98
H.append(("Bauhaus", "Primary-colour Bauhaus composition: circle, square and a black cone.", "Bold",
    '<rect width="1024" height="1024" fill="#F2EBDD"/><circle cx="330" cy="380" r="220" fill="#E4312B"/><rect x="560" y="520" width="330" height="330" fill="#1F4FB5"/><rect x="560" y="170" width="300" height="80" fill="#F5C518"/>',
    cone(i, "#111111", "#F2EBDD", "#111111", shade=False)))
i = 99
H.append(("Enamel Pin", "Hard-enamel pin: gold metal outlines, glossy enamel fills and a highlight glint.", "Pro",
    bg_grad(i, "#3C3F46", "#1E2024"),
    lg("ep99", "#FFE9A6", "#C99A2E", 0, 0, 1, 1) + '<filter id="pn99"><feDropShadow dx="0" dy="18" stdDeviation="14" flood-opacity=".5"/></filter>'
    '<g filter="url(#pn99)">' + cone(i, OR, "#FFFFFF", OR_D, shade=False, stroke="url(#ep99)", sw=26, gloss=True) + '</g>'
    '<path d="M460,330 L480,300" stroke="#fff" stroke-width="14" stroke-linecap="round" opacity=".9"/>'))
i = 100
topo = ''.join(f'<path d="M{512-r*1.1:.0f},{540} C{512-r*1.1:.0f},{540-r*1.2:.0f} {512+r*1.3:.0f},{540-r*1.1:.0f} {512+r*1.1:.0f},{540+r*.1:.0f} C{512+r*.9:.0f},{540+r:.0f} {512-r:.0f},{540+r*1.1:.0f} {512-r*1.1:.0f},{540}Z" fill="none" stroke="#FF8A00" stroke-width="4" opacity="{.25+.05*(k%3)}"/>' for k, r in enumerate(range(120, 700, 45)))
H.append(("Topographic", "Contour-map lines radiating from the cone like a summit on a trail map.", "Concept",
    '<rect width="1024" height="1024" fill="#FFF8EE"/>' + topo, sh(i, 14, 14, .2) + G(i, C(i, OR, "#fff", OR_D, s=.8, dy=10))))

for name, desc, tag, bg, fg in H:
    add(name, desc, bg, fg, tag)

assert len(designs) == 100

# ---------- exporters ----------
def svg(body, defs=""):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024"><defs>{defs}</defs>{body}</svg>'

def layered(d, clip_d, scale=1.0, shadow=False, rim=True):
    k = (1 - scale) * 512
    body = f'<g transform="translate({k} {k}) scale({scale})">'
    body += f'<clipPath id="mask"><path d="{clip_d}"/></clipPath>'
    if shadow:
        body += ('<filter id="macsh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="12" stdDeviation="14" flood-color="#000" flood-opacity=".3"/></filter>'
                 f'<path d="{clip_d}" fill="#000" filter="url(#macsh)"/>')
    body += f'<g clip-path="url(#mask)">{d["bg"]}{d["fg"]}</g>'
    if rim:
        body += f'<path d="{clip_d}" fill="none" stroke="#fff" stroke-opacity=".18" stroke-width="6"/>'
    return svg(body + "</g>")

CIRCLE = "M512,0 A512,512 0 1 1 511.9,0 Z"
RRECT = "M180,100 H844 A80,80 0 0 1 924,180 V844 A80,80 0 0 1 844,924 H180 A80,80 0 0 1 100,844 V180 A80,80 0 0 1 180,100 Z"

meta = []
for n, d in enumerate(designs, 1):
    sid = f"{n:02d}"
    files = {
        "macos": layered(d, SQ_MAC, 1.0, shadow=True),
        "ios": layered(d, SQ_FULL, 1.0),
        "android": layered(d, CIRCLE, 1.0),
        "linux": layered(d, RRECT, 1.0, shadow=True),
        # Windows Fluent: artwork on a tighter rounded plate
        "windows": layered(d, "M160,120 H864 A40,40 0 0 1 904,160 V864 A40,40 0 0 1 864,904 H160 A40,40 0 0 1 120,864 V160 A40,40 0 0 1 160,120 Z", 1.0, shadow=True),
        "layers-bg": svg(d["bg"]),
        "layers-fg": svg(d["fg"]),
    }
    for plat, content in files.items():
        os.makedirs(f"{OUT}/icons/{plat}", exist_ok=True)
        open(f"{OUT}/icons/{plat}/{sid}.svg", "w").write(content)
    meta.append(dict(id=sid, name=d["name"], desc=d["desc"], tag=d["tag"]))

json.dump(meta, open(f"{OUT}/icons.json", "w"), indent=1)
print("ok", len(meta))
