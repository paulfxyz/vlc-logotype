<div align="center">

<img src=".github/img/banner.png" alt="VLC Logotype — 50 guideline-true icon concepts" width="100%">

<br>

**An unofficial redesign study of the [VLC media player](https://www.videolan.org/vlc/) app icon.**
50 concepts built on Apple's icon grid, adapted to Windows, iOS, Android and Linux, with dock mockups and a tap-to-vote page.

<br>

[![license](https://img.shields.io/badge/license-MIT-0a0a0a?style=for-the-badge&labelColor=282828)](LICENSE)
[![concepts](https://img.shields.io/badge/concepts-50-ff7a00?style=for-the-badge&labelColor=282828)](#-the-50-concepts)
[![platforms](https://img.shields.io/badge/platforms-5-0a0a0a?style=for-the-badge&labelColor=282828)](#-platform-masks)

[![macOS](https://img.shields.io/badge/macOS-squircle%20824%2F1024-0a0a0a?style=flat-square&labelColor=282828&logo=apple&logoColor=ededed)](#-platform-masks)
[![iOS](https://img.shields.io/badge/iOS-full--bleed-0a0a0a?style=flat-square&labelColor=282828&logo=apple&logoColor=ededed)](#-platform-masks)
[![Android](https://img.shields.io/badge/Android-adaptive%20circle-3ddc84?style=flat-square&labelColor=282828&logo=android&logoColor=ededed)](#-platform-masks)
[![Windows](https://img.shields.io/badge/Windows-Fluent%20plate-0078d4?style=flat-square&labelColor=282828)](#-platform-masks)
[![Linux](https://img.shields.io/badge/Linux-GNOME%20dash-0a0a0a?style=flat-square&labelColor=282828&logo=linux&logoColor=ededed)](#-platform-masks)
[![format](https://img.shields.io/badge/format-SVG-ffb13b?style=flat-square&labelColor=282828)](icons/)
[![mockups](https://img.shields.io/badge/mockups-50%20PNG-0a0a0a?style=flat-square&labelColor=282828)](shots/)
[![dependencies](https://img.shields.io/badge/dependencies-0-0a0a0a?style=flat-square&labelColor=282828)](#-stack)
[![build step](https://img.shields.io/badge/build%20step-none-0a0a0a?style=flat-square&labelColor=282828)](#-run-it-locally)
[![votes](https://img.shields.io/badge/votes-no%20database-ff7a00?style=flat-square&labelColor=282828)](#-voting--no-database)
[![hosting](https://img.shields.io/badge/hosting-FTP%20%C2%B7%20Vercel-0a0a0a?style=flat-square&labelColor=282828)](#-deploy)
[![PHP](https://img.shields.io/badge/PHP-8-777bb4?style=flat-square&labelColor=282828&logo=php&logoColor=ededed)](vote.php)
[![JavaScript](https://img.shields.io/badge/JavaScript-vanilla-f7df1e?style=flat-square&labelColor=282828&logo=javascript&logoColor=282828)](index.html)
[![Python](https://img.shields.io/badge/Python-generator-3776ab?style=flat-square&labelColor=282828&logo=python&logoColor=ededed)](tools/gen.py)

**[→ The 50 concepts](#-the-50-concepts)** &nbsp;·&nbsp; **[→ Why redesign it](#-why-redesign-it)** &nbsp;·&nbsp; **[→ Voting](#-voting--no-database)** &nbsp;·&nbsp; **[→ Deploy](#-deploy)**

</div>

---

## 📋 Summary

On macOS, VLC ships a bare traffic cone with no background plate. Every other app in the dock sits on the same rounded square, so VLC looks smaller, off-grid and slightly out of place, especially since macOS 26 Tahoe.

This repository is a free, unsolicited proposal to fix that:

| # | Deliverable | What it is |
|---|---|---|
| **1** | **50 icon concepts** | From a faithful refresh to bolder ideas, each split into a background and a foreground layer |
| **2** | **Platform exports** | Every concept exported with the macOS, iOS, Android, Windows and Linux masks, as SVG |
| **3** | **Dock mockups** | macOS dock, before/after, Windows 11 taskbar, iOS and Android home screens, GNOME dash, live in the page and as PNG |
| **4** | **Voting page** | One static `index.html`: open any concept, see it in every dock, vote. No database |

> [!NOTE]
> Concept work, not affiliated with or endorsed by VideoLAN. The VLC name and cone are trademarks of VideoLAN. The MIT licence covers the code and tooling in this repository.

---

## 🔍 Why redesign it

<div align="center"><img src=".github/img/mockups-30.png" alt="Concept #30 in the macOS dock, Windows taskbar, GNOME dash, iOS and Android" width="100%"></div>

- **Squircle plate.** The body is 824 px on a 1024 px canvas with continuous corners, like every native macOS app.
- **Optical balance.** The cone fills about 60% of the plate, so it carries the same visual weight as its neighbours.
- **Depth, not clutter.** Soft top-lit gradients and a single drop shadow, following Tahoe's layered-icon direction.
- **One source, five masks.** Background and foreground are separate layers, so each platform gets its own correct shape.

---

## 🎨 The 50 concepts

Concept (10) · Bold (6) · Minimal (6) · Soft (6) · 3D (5) · Pro (4) · Tahoe (4) · Retro (4) · Dark (3) · Classic (2)

| | | | | |
|:-:|:-:|:-:|:-:|:-:|
| <img src="icons/macos/01.svg" width="96" alt="Faithful Refresh"><br>**#01 Faithful Refresh**<br><sub>Classic</sub> | <img src="icons/macos/02.svg" width="96" alt="Inverted Orange"><br>**#02 Inverted Orange**<br><sub>Bold</sub> | <img src="icons/macos/03.svg" width="96" alt="Graphite Pro"><br>**#03 Graphite Pro**<br><sub>Pro</sub> | <img src="icons/macos/04.svg" width="96" alt="Liquid Glass"><br>**#04 Liquid Glass**<br><sub>Tahoe</sub> | <img src="icons/macos/05.svg" width="96" alt="Flat Minimal"><br>**#05 Flat Minimal**<br><sub>Minimal</sub> |
| <img src="icons/macos/06.svg" width="96" alt="Sunset"><br>**#06 Sunset**<br><sub>Bold</sub> | <img src="icons/macos/07.svg" width="96" alt="Play Cone"><br>**#07 Play Cone**<br><sub>Concept</sub> | <img src="icons/macos/08.svg" width="96" alt="Soft Neumorphic"><br>**#08 Soft Neumorphic**<br><sub>Soft</sub> | <img src="icons/macos/09.svg" width="96" alt="Round 3D"><br>**#09 Round 3D**<br><sub>3D</sub> | <img src="icons/macos/10.svg" width="96" alt="SF Line"><br>**#10 SF Line**<br><sub>Minimal</sub> |
| <img src="icons/macos/11.svg" width="96" alt="8-Bit"><br>**#11 8-Bit**<br><sub>Retro</sub> | <img src="icons/macos/12.svg" width="96" alt="Film Reel"><br>**#12 Film Reel**<br><sub>Concept</sub> | <img src="icons/macos/13.svg" width="96" alt="Blueprint"><br>**#13 Blueprint**<br><sub>Concept</sub> | <img src="icons/macos/14.svg" width="96" alt="Neon Night"><br>**#14 Neon Night**<br><sub>Dark</sub> | <img src="icons/macos/15.svg" width="96" alt="Mono Tint"><br>**#15 Mono Tint**<br><sub>Minimal</sub> |
| <img src="icons/macos/16.svg" width="96" alt="Top View"><br>**#16 Top View**<br><sub>Concept</sub> | <img src="icons/macos/17.svg" width="96" alt="Studio Real"><br>**#17 Studio Real**<br><sub>3D</sub> | <img src="icons/macos/18.svg" width="96" alt="Paper Cut"><br>**#18 Paper Cut**<br><sub>Soft</sub> | <img src="icons/macos/19.svg" width="96" alt="Lens"><br>**#19 Lens**<br><sub>Concept</sub> | <img src="icons/macos/20.svg" width="96" alt="Aqua Candy"><br>**#20 Aqua Candy**<br><sub>Retro</sub> |
| <img src="icons/macos/21.svg" width="96" alt="Cone + VLC"><br>**#21 Cone + VLC**<br><sub>Classic</sub> | <img src="icons/macos/22.svg" width="96" alt="Sound Waves"><br>**#22 Sound Waves**<br><sub>Concept</sub> | <img src="icons/macos/23.svg" width="96" alt="Split Tone"><br>**#23 Split Tone**<br><sub>Bold</sub> | <img src="icons/macos/24.svg" width="96" alt="On Screen"><br>**#24 On Screen**<br><sub>Concept</sub> | <img src="icons/macos/25.svg" width="96" alt="Holo"><br>**#25 Holo**<br><sub>Bold</sub> |
| <img src="icons/macos/26.svg" width="96" alt="Hazard"><br>**#26 Hazard**<br><sub>Bold</sub> | <img src="icons/macos/27.svg" width="96" alt="Cone Button"><br>**#27 Cone Button**<br><sub>Pro</sub> | <img src="icons/macos/28.svg" width="96" alt="Pastel"><br>**#28 Pastel**<br><sub>Soft</sub> | <img src="icons/macos/29.svg" width="96" alt="Clay 3D"><br>**#29 Clay 3D**<br><sub>3D</sub> | <img src="icons/macos/30.svg" width="96" alt="Tahoe Layered"><br>**#30 Tahoe Layered**<br><sub>Tahoe</sub> |
| <img src="icons/macos/31.svg" width="96" alt="Ember"><br>**#31 Ember**<br><sub>Dark</sub> | <img src="icons/macos/32.svg" width="96" alt="Duotone"><br>**#32 Duotone**<br><sub>Bold</sub> | <img src="icons/macos/33.svg" width="96" alt="Low Poly"><br>**#33 Low Poly**<br><sub>3D</sub> | <img src="icons/macos/34.svg" width="96" alt="Sticker"><br>**#34 Sticker**<br><sub>Soft</sub> | <img src="icons/macos/35.svg" width="96" alt="Black & Gold"><br>**#35 Black & Gold**<br><sub>Pro</sub> |
| <img src="icons/macos/36.svg" width="96" alt="Watercolour"><br>**#36 Watercolour**<br><sub>Soft</sub> | <img src="icons/macos/37.svg" width="96" alt="Stacked Bars"><br>**#37 Stacked Bars**<br><sub>Minimal</sub> | <img src="icons/macos/38.svg" width="96" alt="Long Shadow"><br>**#38 Long Shadow**<br><sub>Minimal</sub> | <img src="icons/macos/39.svg" width="96" alt="Chrome"><br>**#39 Chrome**<br><sub>3D</sub> | <img src="icons/macos/40.svg" width="96" alt="Terminal"><br>**#40 Terminal**<br><sub>Retro</sub> |
| <img src="icons/macos/41.svg" width="96" alt="Monogram V"><br>**#41 Monogram V**<br><sub>Concept</sub> | <img src="icons/macos/42.svg" width="96" alt="Mascot"><br>**#42 Mascot**<br><sub>Soft</sub> | <img src="icons/macos/43.svg" width="96" alt="Aurora Glass"><br>**#43 Aurora Glass**<br><sub>Tahoe</sub> | <img src="icons/macos/44.svg" width="96" alt="Material You"><br>**#44 Material You**<br><sub>Minimal</sub> | <img src="icons/macos/45.svg" width="96" alt="Fluent"><br>**#45 Fluent**<br><sub>Pro</sub> |
| <img src="icons/macos/46.svg" width="96" alt="Night Sky"><br>**#46 Night Sky**<br><sub>Dark</sub> | <img src="icons/macos/47.svg" width="96" alt="Wireframe"><br>**#47 Wireframe**<br><sub>Concept</sub> | <img src="icons/macos/48.svg" width="96" alt="Retro Rainbow"><br>**#48 Retro Rainbow**<br><sub>Retro</sub> | <img src="icons/macos/49.svg" width="96" alt="Ribbon Play"><br>**#49 Ribbon Play**<br><sub>Concept</sub> | <img src="icons/macos/50.svg" width="96" alt="Tahoe Dark"><br>**#50 Tahoe Dark**<br><sub>Tahoe</sub> |

<details>
<summary><b>Full list with descriptions and downloads</b></summary>

| # | Name | Family | Idea | Files |
|---|---|---|---|---|
| `01` | Faithful Refresh | Classic | The current cone, finally sitting on a proper macOS squircle with a warm off-white plate. | [macOS](icons/macos/01.svg) · [iOS](icons/ios/01.svg) · [Android](icons/android/01.svg) · [Windows](icons/windows/01.svg) · [Linux](icons/linux/01.svg) · [mockups](shots/01.png) |
| `02` | Inverted Orange | Bold | Brand orange becomes the plate; a crisp white cone with orange stripes. | [macOS](icons/macos/02.svg) · [iOS](icons/ios/02.svg) · [Android](icons/android/02.svg) · [Windows](icons/windows/02.svg) · [Linux](icons/linux/02.svg) · [mockups](shots/02.png) |
| `03` | Graphite Pro | Pro | Pro-app dark graphite plate (think Final Cut / Logic) with a luminous cone. | [macOS](icons/macos/03.svg) · [iOS](icons/ios/03.svg) · [Android](icons/android/03.svg) · [Windows](icons/windows/03.svg) · [Linux](icons/linux/03.svg) · [mockups](shots/03.png) |
| `04` | Liquid Glass | Tahoe | macOS Tahoe style: frosted translucent cone floating over a warm gradient field. | [macOS](icons/macos/04.svg) · [iOS](icons/ios/04.svg) · [Android](icons/android/04.svg) · [Windows](icons/windows/04.svg) · [Linux](icons/linux/04.svg) · [mockups](shots/04.png) |
| `05` | Flat Minimal | Minimal | One colour, one shape. White silhouette with a single negative stripe. | [macOS](icons/macos/05.svg) · [iOS](icons/ios/05.svg) · [Android](icons/android/05.svg) · [Windows](icons/windows/05.svg) · [Linux](icons/linux/05.svg) · [mockups](shots/05.png) |
| `06` | Sunset | Bold | Orange-to-magenta evening gradient, playful and modern. | [macOS](icons/macos/06.svg) · [iOS](icons/ios/06.svg) · [Android](icons/android/06.svg) · [Windows](icons/windows/06.svg) · [Linux](icons/linux/06.svg) · [mockups](shots/06.png) |
| `07` | Play Cone | Concept | The cone's middle stripe is replaced by a play triangle: media player at a glance. | [macOS](icons/macos/07.svg) · [iOS](icons/ios/07.svg) · [Android](icons/android/07.svg) · [Windows](icons/windows/07.svg) · [Linux](icons/linux/07.svg) · [mockups](shots/07.png) |
| `08` | Soft Neumorphic | Soft | Embossed cone pressed out of a pale warm surface. | [macOS](icons/macos/08.svg) · [iOS](icons/ios/08.svg) · [Android](icons/android/08.svg) · [Windows](icons/windows/08.svg) · [Linux](icons/linux/08.svg) · [mockups](shots/08.png) |
| `09` | Round 3D | 3D | A true conical body with curved stripes and elliptical base. | [macOS](icons/macos/09.svg) · [iOS](icons/ios/09.svg) · [Android](icons/android/09.svg) · [Windows](icons/windows/09.svg) · [Linux](icons/linux/09.svg) · [mockups](shots/09.png) |
| `10` | SF Line | Minimal | SF Symbols-style monoline cone in white on orange; ultra-legible at 16px. | [macOS](icons/macos/10.svg) · [iOS](icons/ios/10.svg) · [Android](icons/android/10.svg) · [Windows](icons/windows/10.svg) · [Linux](icons/linux/10.svg) · [mockups](shots/10.png) |
| `11` | 8-Bit | Retro | Retro pixel-art cone for the nostalgic. Crisp at every integer scale. | [macOS](icons/macos/11.svg) · [iOS](icons/ios/11.svg) · [Android](icons/android/11.svg) · [Windows](icons/windows/11.svg) · [Linux](icons/linux/11.svg) · [mockups](shots/11.png) |
| `12` | Film Reel | Concept | The cone sits inside a film-reel ring, nodding to VLC's cinema roots. | [macOS](icons/macos/12.svg) · [iOS](icons/ios/12.svg) · [Android](icons/android/12.svg) · [Windows](icons/windows/12.svg) · [Linux](icons/linux/12.svg) · [mockups](shots/12.png) |
| `13` | Blueprint | Concept | Technical drawing of the cone on blueprint paper. For the engineers. | [macOS](icons/macos/13.svg) · [iOS](icons/ios/13.svg) · [Android](icons/android/13.svg) · [Windows](icons/windows/13.svg) · [Linux](icons/linux/13.svg) · [mockups](shots/13.png) |
| `14` | Neon Night | Dark | Glowing neon-tube cone on midnight navy. Pops in a dark dock. | [macOS](icons/macos/14.svg) · [iOS](icons/ios/14.svg) · [Android](icons/android/14.svg) · [Windows](icons/windows/14.svg) · [Linux](icons/linux/14.svg) · [mockups](shots/14.png) |
| `15` | Mono Tint | Minimal | Built for macOS/iOS tinted & clear modes: pure greyscale that adapts to any accent. | [macOS](icons/macos/15.svg) · [iOS](icons/ios/15.svg) · [Android](icons/android/15.svg) · [Windows](icons/windows/15.svg) · [Linux](icons/linux/15.svg) · [mockups](shots/15.png) |
| `16` | Top View | Concept | Abstract bird's-eye cone: concentric orange and white rings with a play core. | [macOS](icons/macos/16.svg) · [iOS](icons/ios/16.svg) · [Android](icons/android/16.svg) · [Windows](icons/windows/16.svg) · [Linux](icons/linux/16.svg) · [mockups](shots/16.png) |
| `17` | Studio Real | 3D | Photo-studio realism: glossy plastic, soft floor shadow, gentle vignette. | [macOS](icons/macos/17.svg) · [iOS](icons/ios/17.svg) · [Android](icons/android/17.svg) · [Windows](icons/windows/17.svg) · [Linux](icons/linux/17.svg) · [mockups](shots/17.png) |
| `18` | Paper Cut | Soft | Layered paper look: stacked cut-outs with tiny shadows between layers. | [macOS](icons/macos/18.svg) · [iOS](icons/ios/18.svg) · [Android](icons/android/18.svg) · [Windows](icons/windows/18.svg) · [Linux](icons/linux/18.svg) · [mockups](shots/18.png) |
| `19` | Lens | Concept | A glass lens magnifying the cone. Media optics metaphor. | [macOS](icons/macos/19.svg) · [iOS](icons/ios/19.svg) · [Android](icons/android/19.svg) · [Windows](icons/windows/19.svg) · [Linux](icons/linux/19.svg) · [mockups](shots/19.png) |
| `20` | Aqua Candy | Retro | A love letter to Mac OS X Aqua: jelly-glossy cone with a big highlight. | [macOS](icons/macos/20.svg) · [iOS](icons/ios/20.svg) · [Android](icons/android/20.svg) · [Windows](icons/windows/20.svg) · [Linux](icons/linux/20.svg) · [mockups](shots/20.png) |
| `21` | Cone + VLC | Classic | Cone with a clean VLC wordmark underneath — helps recognition at large sizes. | [macOS](icons/macos/21.svg) · [iOS](icons/ios/21.svg) · [Android](icons/android/21.svg) · [Windows](icons/windows/21.svg) · [Linux](icons/linux/21.svg) · [mockups](shots/21.png) |
| `22` | Sound Waves | Concept | Cone emitting audio arcs: equal weight on audio and video playback. | [macOS](icons/macos/22.svg) · [iOS](icons/ios/22.svg) · [Android](icons/android/22.svg) · [Windows](icons/windows/22.svg) · [Linux](icons/linux/22.svg) · [mockups](shots/22.png) |
| `23` | Split Tone | Bold | Half light, half shadow — a graphic, poster-like cone. | [macOS](icons/macos/23.svg) · [iOS](icons/ios/23.svg) · [Android](icons/android/23.svg) · [Windows](icons/windows/23.svg) · [Linux](icons/linux/23.svg) · [mockups](shots/23.png) |
| `24` | On Screen | Concept | A tiny display frame with the cone inside — reads as a video player instantly. | [macOS](icons/macos/24.svg) · [iOS](icons/ios/24.svg) · [Android](icons/android/24.svg) · [Windows](icons/windows/24.svg) · [Linux](icons/linux/24.svg) · [mockups](shots/24.png) |
| `25` | Holo | Bold | Iridescent holographic plate with a chrome-white cone. | [macOS](icons/macos/25.svg) · [iOS](icons/ios/25.svg) · [Android](icons/android/25.svg) · [Windows](icons/windows/25.svg) · [Linux](icons/linux/25.svg) · [mockups](shots/25.png) |
| `26` | Hazard | Bold | Brutalist black-and-orange hazard stripes, cone knocked out in white. | [macOS](icons/macos/26.svg) · [iOS](icons/ios/26.svg) · [Android](icons/android/26.svg) · [Windows](icons/windows/26.svg) · [Linux](icons/linux/26.svg) · [mockups](shots/26.png) |
| `27` | Cone Button | Pro | The cone inside a circular play-button bezel, like a transport control. | [macOS](icons/macos/27.svg) · [iOS](icons/ios/27.svg) · [Android](icons/android/27.svg) · [Windows](icons/windows/27.svg) · [Linux](icons/linux/27.svg) · [mockups](shots/27.png) |
| `28` | Pastel | Soft | Peach-and-cream pastel palette: calm, friendly, very 2020s. | [macOS](icons/macos/28.svg) · [iOS](icons/ios/28.svg) · [Android](icons/android/28.svg) · [Windows](icons/windows/28.svg) · [Linux](icons/linux/28.svg) · [mockups](shots/28.png) |
| `29` | Clay 3D | 3D | Soft clay render: rounded edges, matte material, generous ambient occlusion. | [macOS](icons/macos/29.svg) · [iOS](icons/ios/29.svg) · [Android](icons/android/29.svg) · [Windows](icons/windows/29.svg) · [Linux](icons/linux/29.svg) · [mockups](shots/29.png) |
| `30` | Tahoe Layered | Tahoe | Guideline-true macOS 26 icon: layered foreground, specular edge light, subtle gradient plate. | [macOS](icons/macos/30.svg) · [iOS](icons/ios/30.svg) · [Android](icons/android/30.svg) · [Windows](icons/windows/30.svg) · [Linux](icons/linux/30.svg) · [mockups](shots/30.png) |
| `31` | Ember | Dark | Dark plate with a warm ember glow rising behind a glossy cone. | [macOS](icons/macos/31.svg) · [iOS](icons/ios/31.svg) · [Android](icons/android/31.svg) · [Windows](icons/windows/31.svg) · [Linux](icons/linux/31.svg) · [mockups](shots/31.png) |
| `32` | Duotone | Bold | Two-tone yellow and orange, no white at all. Warm, poster-flat and very legible. | [macOS](icons/macos/32.svg) · [iOS](icons/ios/32.svg) · [Android](icons/android/32.svg) · [Windows](icons/windows/32.svg) · [Linux](icons/linux/32.svg) · [mockups](shots/32.png) |
| `33` | Low Poly | 3D | Faceted, low-polygon cone. Reads as 3D with only four flat shapes. | [macOS](icons/macos/33.svg) · [iOS](icons/ios/33.svg) · [Android](icons/android/33.svg) · [Windows](icons/windows/33.svg) · [Linux](icons/linux/33.svg) · [mockups](shots/33.png) |
| `34` | Sticker | Soft | Die-cut sticker with a thick white border and a slight tilt: playful, laptop-lid energy. | [macOS](icons/macos/34.svg) · [iOS](icons/ios/34.svg) · [Android](icons/android/34.svg) · [Windows](icons/windows/34.svg) · [Linux](icons/linux/34.svg) · [mockups](shots/34.png) |
| `35` | Black & Gold | Pro | Luxury edition: matte black plate, brushed-gold cone. For a Pro-tier look. | [macOS](icons/macos/35.svg) · [iOS](icons/ios/35.svg) · [Android](icons/android/35.svg) · [Windows](icons/windows/35.svg) · [Linux](icons/linux/35.svg) · [mockups](shots/35.png) |
| `36` | Watercolour | Soft | Hand-painted feel: soft pigment blooms behind a clean cone. | [macOS](icons/macos/36.svg) · [iOS](icons/ios/36.svg) · [Android](icons/android/36.svg) · [Windows](icons/windows/36.svg) · [Linux](icons/linux/36.svg) · [mockups](shots/36.png) |
| `37` | Stacked Bars | Minimal | Abstract cone built from five rounded bars, like an equaliser turned sideways. | [macOS](icons/macos/37.svg) · [iOS](icons/ios/37.svg) · [Android](icons/android/37.svg) · [Windows](icons/windows/37.svg) · [Linux](icons/linux/37.svg) · [mockups](shots/37.png) |
| `38` | Long Shadow | Minimal | Flat design classic: white cone casting a 45° long shadow across the plate. | [macOS](icons/macos/38.svg) · [iOS](icons/ios/38.svg) · [Android](icons/android/38.svg) · [Windows](icons/windows/38.svg) · [Linux](icons/linux/38.svg) · [mockups](shots/38.png) |
| `39` | Chrome | 3D | Polished liquid-metal cone with an orange reflection band. | [macOS](icons/macos/39.svg) · [iOS](icons/ios/39.svg) · [Android](icons/android/39.svg) · [Windows](icons/windows/39.svg) · [Linux](icons/linux/39.svg) · [mockups](shots/39.png) |
| `40` | Terminal | Retro | ASCII-art cone in a terminal window, for the command-line crowd. | [macOS](icons/macos/40.svg) · [iOS](icons/ios/40.svg) · [Android](icons/android/40.svg) · [Windows](icons/windows/40.svg) · [Linux](icons/linux/40.svg) · [mockups](shots/40.png) |
| `41` | Monogram V | Concept | The cone flipped into a V for VLC — the stripes still say 'traffic cone'. | [macOS](icons/macos/41.svg) · [iOS](icons/ios/41.svg) · [Android](icons/android/41.svg) · [Windows](icons/windows/41.svg) · [Linux](icons/linux/41.svg) · [mockups](shots/41.png) |
| `42` | Mascot | Soft | A friendly cone character with eyes and a smile. Kid-friendly and memorable. | [macOS](icons/macos/42.svg) · [iOS](icons/ios/42.svg) · [Android](icons/android/42.svg) · [Windows](icons/windows/42.svg) · [Linux](icons/linux/42.svg) · [mockups](shots/42.png) |
| `43` | Aurora Glass | Tahoe | Dark glassmorphism: blurred aurora blobs under a frosted cone. | [macOS](icons/macos/43.svg) · [iOS](icons/ios/43.svg) · [Android](icons/android/43.svg) · [Windows](icons/windows/43.svg) · [Linux](icons/linux/43.svg) · [mockups](shots/43.png) |
| `44` | Material You | Minimal | Android 12+ tonal palette: soft peach container, deep-orange monochrome glyph. | [macOS](icons/macos/44.svg) · [iOS](icons/ios/44.svg) · [Android](icons/android/44.svg) · [Windows](icons/windows/44.svg) · [Linux](icons/linux/44.svg) · [mockups](shots/44.png) |
| `45` | Fluent | Pro | Windows 11 Fluent style: soft gradient cone with a subtle acrylic base, made for the taskbar. | [macOS](icons/macos/45.svg) · [iOS](icons/ios/45.svg) · [Android](icons/android/45.svg) · [Windows](icons/windows/45.svg) · [Linux](icons/linux/45.svg) · [mockups](shots/45.png) |
| `46` | Night Sky | Dark | A cone under a starry sky, with a warm glow on the horizon. Movie-night mood. | [macOS](icons/macos/46.svg) · [iOS](icons/ios/46.svg) · [Android](icons/android/46.svg) · [Windows](icons/windows/46.svg) · [Linux](icons/linux/46.svg) · [mockups](shots/46.png) |
| `47` | Wireframe | Concept | 3D mesh wireframe of the cone, glowing on a dark grid. Engineering chic. | [macOS](icons/macos/47.svg) · [iOS](icons/ios/47.svg) · [Android](icons/android/47.svg) · [Windows](icons/windows/47.svg) · [Linux](icons/linux/47.svg) · [mockups](shots/47.png) |
| `48` | Retro Rainbow | Retro | Six-stripe rainbow cone, a nod to 1980s Mac heritage. | [macOS](icons/macos/48.svg) · [iOS](icons/ios/48.svg) · [Android](icons/android/48.svg) · [Windows](icons/windows/48.svg) · [Linux](icons/linux/48.svg) · [mockups](shots/48.png) |
| `49` | Ribbon Play | Concept | A single orange ribbon folds into a cone shape and a play triangle at once. | [macOS](icons/macos/49.svg) · [iOS](icons/ios/49.svg) · [Android](icons/android/49.svg) · [Windows](icons/windows/49.svg) · [Linux](icons/linux/49.svg) · [mockups](shots/49.png) |
| `50` | Tahoe Dark | Tahoe | Dark-mode twin of Tahoe Layered: graphite plate, same layered cone and edge light. | [macOS](icons/macos/50.svg) · [iOS](icons/ios/50.svg) · [Android](icons/android/50.svg) · [Windows](icons/windows/50.svg) · [Linux](icons/linux/50.svg) · [mockups](shots/50.png) |

</details>

<div align="center"><img src=".github/img/contact-sheet.png" alt="Contact sheet of all 50 concepts" width="100%"></div>

---

## 🧩 Platform masks

| Platform | Folder | Shape |
|---|---|---|
| macOS | [`icons/macos/`](icons/macos/) | 824/1024 squircle with padding, rim light and drop shadow (Apple grid) |
| iOS / iPadOS | [`icons/ios/`](icons/ios/) | Full-bleed squircle; the system applies its own mask |
| Android | [`icons/android/`](icons/android/) | Adaptive icon preview, circle mask |
| Windows 11 | [`icons/windows/`](icons/windows/) | Fluent-style rounded plate |
| Linux (GNOME) | [`icons/linux/`](icons/linux/) | Adwaita-style rounded square |
| Layers | [`icons/layers-bg/`](icons/layers-bg/) · [`icons/layers-fg/`](icons/layers-fg/) | Raw background and foreground, for Icon Composer or Android adaptive icons |

---

## 🗳️ Voting — no database

Open a concept, check it in every dock, then tap **Vote**. Tap again to undo. Each browser gets a random voter ID in a cookie, and the server keeps one vote per voter per concept.

| Backend | File | Storage |
|---|---|---|
| Any PHP host (FTP) | [`vote.php`](vote.php) | `votes.json` next to the page, written with a file lock; [`.htaccess`](.htaccess) blocks direct download on Apache |
| Vercel | [`api/votes.js`](api/votes.js) | Vercel Blob, one empty file per vote (`votes/<id>/<voter>`), counted by listing |
| Local / any VPS | [`server/server.py`](server/server.py) | `data/votes.json`, Python standard library only |

The page picks the endpoint automatically (`vote.php`, or `/api/votes` on `*.vercel.app`). Set `window.VOTE_API` before the main script to point it anywhere else.

> [!WARNING]
> Votes are anonymous and unauthenticated. The voter ID is hashed with the IP address, which makes stuffing harder but not impossible. Treat the tally as a signal, not a poll.

---

## 🚀 Deploy

**FTP / shared hosting**

1. Upload the repository contents (at minimum `index.html`, `icons/`, `icons.json`, `shots/`, `vote.php`, `.htaccess`).
2. Make the folder writable by PHP (`chmod 775`) so `votes.json` can be created.

**Vercel**

```bash
vercel link
vercel blob create-store vlc-logotype   # connect it to the project so BLOB_READ_WRITE_TOKEN is set
vercel deploy --prod
```

---

## 💻 Run it locally

```bash
python3 server/server.py &          # vote API on :8787 (optional)
python3 -m http.server 8099          # then open http://localhost:8099
```

Without a reachable vote endpoint the page still works and keeps votes for the current visit only.

---

## 🛠️ Stack

- **Icons** — hand-written SVG generated by [`tools/gen.py`](tools/gen.py) (Python standard library). Edit a concept, run `python3 tools/gen.py`, every platform export updates.
- **Mockups** — plain HTML and CSS inside [`index.html`](index.html); `?shot=<id>` renders the export layout.
- **Screenshots** — [`tools/shots.py`](tools/shots.py) with Playwright.
- **Page** — one file, vanilla JavaScript, no framework, no build step.

```
index.html          voting page + all dock mockups
icons.json          concept registry (id, name, family, description)
icons/<platform>/   50 SVGs per platform + raw layers
shots/              50 PNG mockup sheets
vote.php            PHP vote endpoint (FTP hosting)
api/votes.js        Vercel function (Vercel Blob)
server/server.py    standalone Python vote server
tools/              gen.py (icons) · shots.py (PNG export)
```

---

## 📄 License

[MIT](LICENSE) © Paul Fleury. VLC and the VLC cone are trademarks of VideoLAN; this is an independent design proposal.
