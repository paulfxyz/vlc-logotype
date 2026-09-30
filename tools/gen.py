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

assert len(designs) == 50

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
