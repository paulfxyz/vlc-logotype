<div align="center">

<img src=".github/img/banner.png" alt="VLC Logotype: 100 icon concepts for macOS, Windows, iOS, Android and Linux" width="100%">

<br>

**An unofficial redesign study of the [VLC media player](https://www.videolan.org/vlc/) app icon.**<br>
100 concepts built on Apple's icon grid and adapted to Windows, iOS, Android and Linux, with dock mockups and a tap-to-vote page.

Everything is live at **[paulfleury.com/vlc](https://paulfleury.com/vlc/)**. Prefer not to clone? Grab the whole site in one archive: **[dump.zip](https://paulfleury.com/vlc/dump.zip)**.

<br>

[![license: MIT](https://img.shields.io/badge/license-MIT-0a0a0a?style=for-the-badge&labelColor=282828)](LICENSE)
[![live: paulfleury.com/vlc](https://img.shields.io/badge/live-paulfleury.com%2Fvlc-ff7a00?style=for-the-badge&labelColor=282828)](https://paulfleury.com/vlc/)
[![download: dump.zip](https://img.shields.io/badge/download-dump.zip-0a0a0a?style=for-the-badge&labelColor=282828)](https://paulfleury.com/vlc/dump.zip)

[![concepts: 100](https://img.shields.io/badge/concepts-100-ff7a00?style=flat-square&labelColor=282828)](#-the-concepts)
[![design directions: 67](https://img.shields.io/badge/design%20directions-67-0a0a0a?style=flat-square&labelColor=282828)](#-design-directions)
[![holiday editions: 33](https://img.shields.io/badge/holiday%20editions-33-0a0a0a?style=flat-square&labelColor=282828)](#-holiday-editions)
[![macOS: 824/1024 squircle](https://img.shields.io/badge/macOS-824%2F1024%20squircle-0a0a0a?style=flat-square&labelColor=282828&logo=apple&logoColor=ededed)](#-platform-exports)
[![iOS: full-bleed](https://img.shields.io/badge/iOS-full--bleed-0a0a0a?style=flat-square&labelColor=282828&logo=apple&logoColor=ededed)](#-platform-exports)
[![Android: adaptive circle](https://img.shields.io/badge/Android-adaptive%20circle-3ddc84?style=flat-square&labelColor=282828&logo=android&logoColor=ededed)](#-platform-exports)
[![Windows: Fluent plate](https://img.shields.io/badge/Windows-Fluent%20plate-0078d4?style=flat-square&labelColor=282828)](#-platform-exports)
[![Linux: GNOME dash](https://img.shields.io/badge/Linux-GNOME%20dash-0a0a0a?style=flat-square&labelColor=282828&logo=linux&logoColor=ededed)](#-platform-exports)
[![icons: SVG](https://img.shields.io/badge/icons-SVG-ffb13b?style=flat-square&labelColor=282828)](icons/)
[![mockups: 100 PNG](https://img.shields.io/badge/mockups-100%20PNG-0a0a0a?style=flat-square&labelColor=282828)](shots/)
[![votes: no database](https://img.shields.io/badge/votes-no%20database-ff7a00?style=flat-square&labelColor=282828)](#-voting-without-a-database)
[![vote ledger: counts.json](https://img.shields.io/badge/vote%20ledger-counts.json-0a0a0a?style=flat-square&labelColor=282828)](votes/counts.json)
[![dependencies: 0](https://img.shields.io/badge/dependencies-0-0a0a0a?style=flat-square&labelColor=282828)](#-stack)
[![build step: none](https://img.shields.io/badge/build%20step-none-0a0a0a?style=flat-square&labelColor=282828)](#-run-it-locally)
[![PHP: vote endpoint](https://img.shields.io/badge/PHP-vote%20endpoint-777bb4?style=flat-square&labelColor=282828&logo=php&logoColor=ededed)](vote.php)
[![JavaScript: vanilla](https://img.shields.io/badge/JavaScript-vanilla-f7df1e?style=flat-square&labelColor=282828&logo=javascript&logoColor=282828)](index.html)
[![Python: generator](https://img.shields.io/badge/Python-generator-3776ab?style=flat-square&labelColor=282828&logo=python&logoColor=ededed)](tools/gen.py)
[![vibe designed: Perplexity Computer](https://img.shields.io/badge/vibe%20designed-Perplexity%20Computer-20808d?style=flat-square&labelColor=282828&logo=perplexity&logoColor=ededed)](#-this-is-vibe-designing)

**[→ Open the voting page](https://paulfleury.com/vlc/)** &nbsp;·&nbsp; **[→ The concepts](#-the-concepts)** &nbsp;·&nbsp; **[→ Why redesign it](#-why-redesign-it)** &nbsp;·&nbsp; **[↓ Download](https://paulfleury.com/vlc/dump.zip)**

</div>

---

## 📋 Summary

On macOS, VLC ships a bare traffic cone with no background plate. Every other app in the Dock sits on the same rounded square, so VLC looks smaller, off-grid and slightly out of place, especially since macOS 26 Tahoe.

This repository is a free, unsolicited proposal to fix that.

| # | Deliverable | What it is | Where |
|---|---|---|---|
| **1** | **100 icon concepts** | 67 design directions, from a faithful refresh to bolder ideas, plus 33 holiday editions | [`icons/`](icons/) |
| **2** | **Platform exports** | Every concept as SVG with the macOS, iOS, Android, Windows and Linux masks, plus raw background and foreground layers | [`icons/<platform>/`](icons/) |
| **3** | **Dock mockups** | macOS Dock, before/after, Windows 11 taskbar, iOS and Android home screens, GNOME dash | [`shots/`](shots/) |
| **4** | **Voting page** | One static `index.html`: open a concept, see it in every dock, vote. No database | [paulfleury.com/vlc](https://paulfleury.com/vlc/) |

> [!NOTE]
> Concept work, not affiliated with or endorsed by VideoLAN. "VLC" and the cone are trademarks of VideoLAN. The MIT License covers the code and tooling in this repository.

---

## 🌐 The site

<div align="center"><a href="https://paulfleury.com/vlc/"><img src=".github/img/site.png" alt="The voting page at paulfleury.com/vlc showing 100 concepts" width="100%"></a></div>

Open any concept to see it in the macOS Dock, a before/after, the Windows 11 taskbar, iOS and Android home screens and the GNOME dash, then vote. Filters split the 67 design directions from the 33 holiday editions.

---

## 🔍 Why redesign it

<div align="center"><img src=".github/img/mockups-30.png" alt="Concept #30 in the macOS Dock, Windows taskbar, GNOME dash, iOS and Android" width="100%"></div>

- **Squircle plate.** An 824 px body on a 1024 px canvas with continuous corners, like every native macOS app.
- **Optical balance.** The cone fills about 60% of the plate, so it carries the same visual weight as its neighbours.
- **Depth, not clutter.** Soft top-lit gradients and a single drop shadow, following Tahoe's layered-icon direction.
- **One source, five masks.** Background and foreground are separate layers, so each platform gets its own correct shape.

---

## 🎨 The concepts

<div align="center"><img src=".github/img/contact-sheet.png" alt="Contact sheet of all 100 concepts" width="100%"></div>

### 🧭 Design directions

67 directions: Concept (13) · Bold (9) · Minimal (8) · Soft (8) · Pro (6) · 3D (6) · Retro (6) · Dark (5) · Tahoe (4) · Classic (2).

|   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|
| <img src="icons/macos/01.svg" width="88" alt="Faithful Refresh"><br><b>#01</b> Faithful Refresh | <img src="icons/macos/02.svg" width="88" alt="Inverted Orange"><br><b>#02</b> Inverted Orange | <img src="icons/macos/03.svg" width="88" alt="Graphite Pro"><br><b>#03</b> Graphite Pro | <img src="icons/macos/04.svg" width="88" alt="Liquid Glass"><br><b>#04</b> Liquid Glass | <img src="icons/macos/05.svg" width="88" alt="Flat Minimal"><br><b>#05</b> Flat Minimal |
| <img src="icons/macos/06.svg" width="88" alt="Sunset"><br><b>#06</b> Sunset | <img src="icons/macos/07.svg" width="88" alt="Play Cone"><br><b>#07</b> Play Cone | <img src="icons/macos/08.svg" width="88" alt="Soft Neumorphic"><br><b>#08</b> Soft Neumorphic | <img src="icons/macos/09.svg" width="88" alt="Round 3D"><br><b>#09</b> Round 3D | <img src="icons/macos/10.svg" width="88" alt="SF Line"><br><b>#10</b> SF Line |
| <img src="icons/macos/11.svg" width="88" alt="8-Bit"><br><b>#11</b> 8-Bit | <img src="icons/macos/12.svg" width="88" alt="Film Reel"><br><b>#12</b> Film Reel | <img src="icons/macos/13.svg" width="88" alt="Blueprint"><br><b>#13</b> Blueprint | <img src="icons/macos/14.svg" width="88" alt="Neon Night"><br><b>#14</b> Neon Night | <img src="icons/macos/15.svg" width="88" alt="Mono Tint"><br><b>#15</b> Mono Tint |
| <img src="icons/macos/16.svg" width="88" alt="Top View"><br><b>#16</b> Top View | <img src="icons/macos/17.svg" width="88" alt="Studio Real"><br><b>#17</b> Studio Real | <img src="icons/macos/18.svg" width="88" alt="Paper Cut"><br><b>#18</b> Paper Cut | <img src="icons/macos/19.svg" width="88" alt="Lens"><br><b>#19</b> Lens | <img src="icons/macos/20.svg" width="88" alt="Aqua Candy"><br><b>#20</b> Aqua Candy |
| <img src="icons/macos/21.svg" width="88" alt="Cone + VLC"><br><b>#21</b> Cone + VLC | <img src="icons/macos/22.svg" width="88" alt="Sound Waves"><br><b>#22</b> Sound Waves | <img src="icons/macos/23.svg" width="88" alt="Split Tone"><br><b>#23</b> Split Tone | <img src="icons/macos/24.svg" width="88" alt="On Screen"><br><b>#24</b> On Screen | <img src="icons/macos/25.svg" width="88" alt="Holo"><br><b>#25</b> Holo |
| <img src="icons/macos/26.svg" width="88" alt="Hazard"><br><b>#26</b> Hazard | <img src="icons/macos/27.svg" width="88" alt="Cone Button"><br><b>#27</b> Cone Button | <img src="icons/macos/28.svg" width="88" alt="Pastel"><br><b>#28</b> Pastel | <img src="icons/macos/29.svg" width="88" alt="Clay 3D"><br><b>#29</b> Clay 3D | <img src="icons/macos/30.svg" width="88" alt="Tahoe Layered"><br><b>#30</b> Tahoe Layered |
| <img src="icons/macos/31.svg" width="88" alt="Ember"><br><b>#31</b> Ember | <img src="icons/macos/32.svg" width="88" alt="Duotone"><br><b>#32</b> Duotone | <img src="icons/macos/33.svg" width="88" alt="Low Poly"><br><b>#33</b> Low Poly | <img src="icons/macos/34.svg" width="88" alt="Sticker"><br><b>#34</b> Sticker | <img src="icons/macos/35.svg" width="88" alt="Black & Gold"><br><b>#35</b> Black & Gold |
| <img src="icons/macos/36.svg" width="88" alt="Watercolour"><br><b>#36</b> Watercolour | <img src="icons/macos/37.svg" width="88" alt="Stacked Bars"><br><b>#37</b> Stacked Bars | <img src="icons/macos/38.svg" width="88" alt="Long Shadow"><br><b>#38</b> Long Shadow | <img src="icons/macos/39.svg" width="88" alt="Chrome"><br><b>#39</b> Chrome | <img src="icons/macos/40.svg" width="88" alt="Terminal"><br><b>#40</b> Terminal |
| <img src="icons/macos/41.svg" width="88" alt="Monogram V"><br><b>#41</b> Monogram V | <img src="icons/macos/42.svg" width="88" alt="Mascot"><br><b>#42</b> Mascot | <img src="icons/macos/43.svg" width="88" alt="Aurora Glass"><br><b>#43</b> Aurora Glass | <img src="icons/macos/44.svg" width="88" alt="Material You"><br><b>#44</b> Material You | <img src="icons/macos/45.svg" width="88" alt="Fluent"><br><b>#45</b> Fluent |
| <img src="icons/macos/46.svg" width="88" alt="Night Sky"><br><b>#46</b> Night Sky | <img src="icons/macos/47.svg" width="88" alt="Wireframe"><br><b>#47</b> Wireframe | <img src="icons/macos/48.svg" width="88" alt="Retro Rainbow"><br><b>#48</b> Retro Rainbow | <img src="icons/macos/49.svg" width="88" alt="Ribbon Play"><br><b>#49</b> Ribbon Play | <img src="icons/macos/50.svg" width="88" alt="Tahoe Dark"><br><b>#50</b> Tahoe Dark |
| <img src="icons/macos/84.svg" width="88" alt="Outline Plate"><br><b>#84</b> Outline Plate | <img src="icons/macos/85.svg" width="88" alt="Glitch"><br><b>#85</b> Glitch | <img src="icons/macos/86.svg" width="88" alt="Vaporwave"><br><b>#86</b> Vaporwave | <img src="icons/macos/87.svg" width="88" alt="Marble"><br><b>#87</b> Marble | <img src="icons/macos/88.svg" width="88" alt="Embroidered Patch"><br><b>#88</b> Embroidered Patch |
| <img src="icons/macos/89.svg" width="88" alt="Voxel"><br><b>#89</b> Voxel | <img src="icons/macos/90.svg" width="88" alt="Spotlight"><br><b>#90</b> Spotlight | <img src="icons/macos/91.svg" width="88" alt="Origami"><br><b>#91</b> Origami | <img src="icons/macos/92.svg" width="88" alt="Stencil"><br><b>#92</b> Stencil | <img src="icons/macos/93.svg" width="88" alt="Halftone Pop"><br><b>#93</b> Halftone Pop |
| <img src="icons/macos/94.svg" width="88" alt="Melt"><br><b>#94</b> Melt | <img src="icons/macos/95.svg" width="88" alt="Constellation"><br><b>#95</b> Constellation | <img src="icons/macos/96.svg" width="88" alt="Tangram"><br><b>#96</b> Tangram | <img src="icons/macos/97.svg" width="88" alt="Negative Space"><br><b>#97</b> Negative Space | <img src="icons/macos/98.svg" width="88" alt="Bauhaus"><br><b>#98</b> Bauhaus |
| <img src="icons/macos/99.svg" width="88" alt="Enamel Pin"><br><b>#99</b> Enamel Pin | <img src="icons/macos/100.svg" width="88" alt="Topographic"><br><b>#100</b> Topographic |   |   |   |

<details>
<summary><b>All 67 design directions, with descriptions and downloads</b></summary>

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
| `84` | Outline Plate | Minimal | Stroke-only plate and cone in brand orange on near-black. Quiet, crisp, very Pro. | [macOS](icons/macos/84.svg) · [iOS](icons/ios/84.svg) · [Android](icons/android/84.svg) · [Windows](icons/windows/84.svg) · [Linux](icons/linux/84.svg) · [mockups](shots/84.png) |
| `85` | Glitch | Retro | RGB-split glitch cone with scanlines, for a VHS-era vibe. | [macOS](icons/macos/85.svg) · [iOS](icons/ios/85.svg) · [Android](icons/android/85.svg) · [Windows](icons/windows/85.svg) · [Linux](icons/linux/85.svg) · [mockups](shots/85.png) |
| `86` | Vaporwave | Retro | Synthwave sunset with a neon grid floor: the cone as a retro-future monument. | [macOS](icons/macos/86.svg) · [iOS](icons/ios/86.svg) · [Android](icons/android/86.svg) · [Windows](icons/windows/86.svg) · [Linux](icons/linux/86.svg) · [mockups](shots/86.png) |
| `87` | Marble | Pro | White Carrara marble plate with gold veining under a gilded cone. | [macOS](icons/macos/87.svg) · [iOS](icons/ios/87.svg) · [Android](icons/android/87.svg) · [Windows](icons/windows/87.svg) · [Linux](icons/linux/87.svg) · [mockups](shots/87.png) |
| `88` | Embroidered Patch | Soft | A stitched round patch with a twill texture — the jacket-sleeve version of VLC. | [macOS](icons/macos/88.svg) · [iOS](icons/ios/88.svg) · [Android](icons/android/88.svg) · [Windows](icons/windows/88.svg) · [Linux](icons/linux/88.svg) · [mockups](shots/88.png) |
| `89` | Voxel | 3D | Isometric voxel cone stacked from orange and white blocks. Very Minecraft, very readable. | [macOS](icons/macos/89.svg) · [iOS](icons/ios/89.svg) · [Android](icons/android/89.svg) · [Windows](icons/windows/89.svg) · [Linux](icons/linux/89.svg) · [mockups](shots/89.png) |
| `90` | Spotlight | Dark | A theatre spotlight beam lands on the cone. Showtime. | [macOS](icons/macos/90.svg) · [iOS](icons/ios/90.svg) · [Android](icons/android/90.svg) · [Windows](icons/windows/90.svg) · [Linux](icons/linux/90.svg) · [mockups](shots/90.png) |
| `91` | Origami | Soft | Folded paper cone: two crisp planes and a paper-white base. | [macOS](icons/macos/91.svg) · [iOS](icons/ios/91.svg) · [Android](icons/android/91.svg) · [Windows](icons/windows/91.svg) · [Linux](icons/linux/91.svg) · [mockups](shots/91.png) |
| `92` | Stencil | Bold | Street-art stencil sprayed on a brick wall, with overspray speckle. | [macOS](icons/macos/92.svg) · [iOS](icons/ios/92.svg) · [Android](icons/android/92.svg) · [Windows](icons/windows/92.svg) · [Linux](icons/linux/92.svg) · [mockups](shots/92.png) |
| `93` | Halftone Pop | Bold | Pop-art comic cone: black ink outlines on a halftone yellow burst. | [macOS](icons/macos/93.svg) · [iOS](icons/ios/93.svg) · [Android](icons/android/93.svg) · [Windows](icons/windows/93.svg) · [Linux](icons/linux/93.svg) · [mockups](shots/93.png) |
| `94` | Melt | Concept | The cone melting like an ice-lolly on a hot day. Surreal, very memorable. | [macOS](icons/macos/94.svg) · [iOS](icons/ios/94.svg) · [Android](icons/android/94.svg) · [Windows](icons/windows/94.svg) · [Linux](icons/linux/94.svg) · [mockups](shots/94.png) |
| `95` | Constellation | Dark | The cone drawn as a star constellation over deep navy. | [macOS](icons/macos/95.svg) · [iOS](icons/ios/95.svg) · [Android](icons/android/95.svg) · [Windows](icons/windows/95.svg) · [Linux](icons/linux/95.svg) · [mockups](shots/95.png) |
| `96` | Tangram | Concept | Seven tangram pieces arranged into a cone. Puzzle-box charm. | [macOS](icons/macos/96.svg) · [iOS](icons/ios/96.svg) · [Android](icons/android/96.svg) · [Windows](icons/windows/96.svg) · [Linux](icons/linux/96.svg) · [mockups](shots/96.png) |
| `97` | Negative Space | Minimal | An orange disc with the cone cut clean out of it. Pure figure-ground. | [macOS](icons/macos/97.svg) · [iOS](icons/ios/97.svg) · [Android](icons/android/97.svg) · [Windows](icons/windows/97.svg) · [Linux](icons/linux/97.svg) · [mockups](shots/97.png) |
| `98` | Bauhaus | Bold | Primary-colour Bauhaus composition: circle, square and a black cone. | [macOS](icons/macos/98.svg) · [iOS](icons/ios/98.svg) · [Android](icons/android/98.svg) · [Windows](icons/windows/98.svg) · [Linux](icons/linux/98.svg) · [mockups](shots/98.png) |
| `99` | Enamel Pin | Pro | Hard-enamel pin: gold metal outlines, glossy enamel fills and a highlight glint. | [macOS](icons/macos/99.svg) · [iOS](icons/ios/99.svg) · [Android](icons/android/99.svg) · [Windows](icons/windows/99.svg) · [Linux](icons/linux/99.svg) · [mockups](shots/99.png) |
| `100` | Topographic | Concept | Contour-map lines radiating from the cone like a summit on a trail map. | [macOS](icons/macos/100.svg) · [iOS](icons/ios/100.svg) · [Android](icons/android/100.svg) · [Windows](icons/windows/100.svg) · [Linux](icons/linux/100.svg) · [mockups](shots/100.png) |

</details>

### 🎉 Holiday editions

33 seasonal variants for the dates people actually celebrate: National (13) · Religious (11) · Seasonal (9). Religious symbols are kept to widely shared, respectful motifs (lights, lanterns, crescents, arches, lotus); no figures are depicted.

<div align="center"><img src=".github/img/mockups-66.png" alt="Holiday edition #66 Halloween in every dock" width="100%"></div>

|   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|
| <img src="icons/macos/51.svg" width="88" alt="Christmas"><br><b>#51</b> Christmas | <img src="icons/macos/52.svg" width="88" alt="Hanukkah"><br><b>#52</b> Hanukkah | <img src="icons/macos/53.svg" width="88" alt="New Year's Eve"><br><b>#53</b> New Year's Eve | <img src="icons/macos/54.svg" width="88" alt="Lunar New Year"><br><b>#54</b> Lunar New Year | <img src="icons/macos/55.svg" width="88" alt="Valentine's Day"><br><b>#55</b> Valentine's Day |
| <img src="icons/macos/56.svg" width="88" alt="St Patrick's Day"><br><b>#56</b> St Patrick's Day | <img src="icons/macos/57.svg" width="88" alt="Easter"><br><b>#57</b> Easter | <img src="icons/macos/58.svg" width="88" alt="Ramadan"><br><b>#58</b> Ramadan | <img src="icons/macos/59.svg" width="88" alt="Eid al-Fitr"><br><b>#59</b> Eid al-Fitr | <img src="icons/macos/60.svg" width="88" alt="Eid al-Adha"><br><b>#60</b> Eid al-Adha |
| <img src="icons/macos/61.svg" width="88" alt="Diwali"><br><b>#61</b> Diwali | <img src="icons/macos/62.svg" width="88" alt="Holi"><br><b>#62</b> Holi | <img src="icons/macos/63.svg" width="88" alt="Navratri"><br><b>#63</b> Navratri | <img src="icons/macos/64.svg" width="88" alt="Rosh Hashanah"><br><b>#64</b> Rosh Hashanah | <img src="icons/macos/65.svg" width="88" alt="Vesak"><br><b>#65</b> Vesak |
| <img src="icons/macos/66.svg" width="88" alt="Halloween"><br><b>#66</b> Halloween | <img src="icons/macos/67.svg" width="88" alt="Día de los Muertos"><br><b>#67</b> Día de los Muertos | <img src="icons/macos/68.svg" width="88" alt="Thanksgiving"><br><b>#68</b> Thanksgiving | <img src="icons/macos/69.svg" width="88" alt="Independence Day (US)"><br><b>#69</b> Independence Day (US) | <img src="icons/macos/70.svg" width="88" alt="Fête nationale (FR)"><br><b>#70</b> Fête nationale (FR) |
| <img src="icons/macos/71.svg" width="88" alt="Oktoberfest"><br><b>#71</b> Oktoberfest | <img src="icons/macos/72.svg" width="88" alt="Carnaval (Rio)"><br><b>#72</b> Carnaval (Rio) | <img src="icons/macos/73.svg" width="88" alt="Pride"><br><b>#73</b> Pride | <img src="icons/macos/74.svg" width="88" alt="King's Day (NL)"><br><b>#74</b> King's Day (NL) | <img src="icons/macos/75.svg" width="88" alt="Canada Day"><br><b>#75</b> Canada Day |
| <img src="icons/macos/76.svg" width="88" alt="Bonfire Night (UK)"><br><b>#76</b> Bonfire Night (UK) | <img src="icons/macos/77.svg" width="88" alt="Songkran"><br><b>#77</b> Songkran | <img src="icons/macos/78.svg" width="88" alt="Nowruz"><br><b>#78</b> Nowruz | <img src="icons/macos/79.svg" width="88" alt="Hanami"><br><b>#79</b> Hanami | <img src="icons/macos/80.svg" width="88" alt="Santo António (Lisboa)"><br><b>#80</b> Santo António (Lisboa) |
| <img src="icons/macos/81.svg" width="88" alt="Earth Day"><br><b>#81</b> Earth Day | <img src="icons/macos/82.svg" width="88" alt="Mid-Autumn Festival"><br><b>#82</b> Mid-Autumn Festival | <img src="icons/macos/83.svg" width="88" alt="Midsummer"><br><b>#83</b> Midsummer |   |   |

<details>
<summary><b>All 33 holiday editions, with dates and downloads</b></summary>

| # | Name | Type | When | Idea | Files |
|---|---|---|---|---|---|
| `51` | Christmas | Religious | Christmas · 25 Dec | a Santa-hat cone with a fur trim and pom-pom, falling snow on festive red. | [macOS](icons/macos/51.svg) · [iOS](icons/ios/51.svg) · [Android](icons/android/51.svg) · [Windows](icons/windows/51.svg) · [Linux](icons/linux/51.svg) · [mockups](shots/51.png) |
| `52` | Hanukkah | Religious | Hanukkah · 8 nights in Kislev | the cone as the shamash, lighting eight candles on deep blue. | [macOS](icons/macos/52.svg) · [iOS](icons/ios/52.svg) · [Android](icons/android/52.svg) · [Windows](icons/windows/52.svg) · [Linux](icons/linux/52.svg) · [mockups](shots/52.png) |
| `53` | New Year's Eve | Seasonal | New Year · 31 Dec | party-hat cone in gold, fireworks and confetti at midnight. | [macOS](icons/macos/53.svg) · [iOS](icons/ios/53.svg) · [Android](icons/android/53.svg) · [Windows](icons/windows/53.svg) · [Linux](icons/linux/53.svg) · [mockups](shots/53.png) |
| `54` | Lunar New Year | Seasonal | Lunar New Year · Jan–Feb | red and gold cone flanked by paper lanterns. | [macOS](icons/macos/54.svg) · [iOS](icons/ios/54.svg) · [Android](icons/android/54.svg) · [Windows](icons/windows/54.svg) · [Linux](icons/linux/54.svg) · [mockups](shots/54.png) |
| `55` | Valentine's Day | Seasonal | Valentine's · 14 Feb | a candy-pink cone with heart confetti. | [macOS](icons/macos/55.svg) · [iOS](icons/ios/55.svg) · [Android](icons/android/55.svg) · [Windows](icons/windows/55.svg) · [Linux](icons/linux/55.svg) · [mockups](shots/55.png) |
| `56` | St Patrick's Day | National | St Patrick's · 17 Mar | Irish green, white and orange cone with a shamrock. | [macOS](icons/macos/56.svg) · [iOS](icons/ios/56.svg) · [Android](icons/android/56.svg) · [Windows](icons/windows/56.svg) · [Linux](icons/linux/56.svg) · [mockups](shots/56.png) |
| `57` | Easter | Religious | Easter · Mar–Apr | a hand-painted egg-pattern cone, pastel eggs at its base. | [macOS](icons/macos/57.svg) · [iOS](icons/ios/57.svg) · [Android](icons/android/57.svg) · [Windows](icons/windows/57.svg) · [Linux](icons/linux/57.svg) · [mockups](shots/57.png) |
| `58` | Ramadan | Religious | Ramadan · 9th month | a glowing fanous lantern and crescent over a calm night. | [macOS](icons/macos/58.svg) · [iOS](icons/ios/58.svg) · [Android](icons/android/58.svg) · [Windows](icons/windows/58.svg) · [Linux](icons/linux/58.svg) · [mockups](shots/58.png) |
| `59` | Eid al-Fitr | Religious | Eid al-Fitr · end of Ramadan | emerald and gold, geometric stars and a festive crescent. | [macOS](icons/macos/59.svg) · [iOS](icons/ios/59.svg) · [Android](icons/android/59.svg) · [Windows](icons/windows/59.svg) · [Linux](icons/linux/59.svg) · [mockups](shots/59.png) |
| `60` | Eid al-Adha | Religious | Eid al-Adha · 10 Dhu al-Hijjah | the cone framed in a warm, pointed arch with a crescent. | [macOS](icons/macos/60.svg) · [iOS](icons/ios/60.svg) · [Android](icons/android/60.svg) · [Windows](icons/windows/60.svg) · [Linux](icons/linux/60.svg) · [mockups](shots/60.png) |
| `61` | Diwali | Religious | Diwali · Oct–Nov | a rangoli bloom, clay diyas and a cone lit like a lamp. | [macOS](icons/macos/61.svg) · [iOS](icons/ios/61.svg) · [Android](icons/android/61.svg) · [Windows](icons/windows/61.svg) · [Linux](icons/linux/61.svg) · [mockups](shots/61.png) |
| `62` | Holi | Religious | Holi · Phalguna full moon | bursts of coloured powder and a paint-splashed cone. | [macOS](icons/macos/62.svg) · [iOS](icons/ios/62.svg) · [Android](icons/android/62.svg) · [Windows](icons/windows/62.svg) · [Linux](icons/linux/62.svg) · [mockups](shots/62.png) |
| `63` | Navratri | Religious | Navratri · nine nights | the nine day-colours as rays behind a white cone. | [macOS](icons/macos/63.svg) · [iOS](icons/ios/63.svg) · [Android](icons/android/63.svg) · [Windows](icons/windows/63.svg) · [Linux](icons/linux/63.svg) · [mockups](shots/63.png) |
| `64` | Rosh Hashanah | Religious | Rosh Hashanah · Tishrei | a sweet new year: apple, honey drop and honey-gold stripes. | [macOS](icons/macos/64.svg) · [iOS](icons/ios/64.svg) · [Android](icons/android/64.svg) · [Windows](icons/windows/64.svg) · [Linux](icons/linux/64.svg) · [mockups](shots/64.png) |
| `65` | Vesak | Religious | Vesak · full moon of Vesākha | the cone rising from a lotus under soft lanterns. | [macOS](icons/macos/65.svg) · [iOS](icons/ios/65.svg) · [Android](icons/android/65.svg) · [Windows](icons/windows/65.svg) · [Linux](icons/linux/65.svg) · [mockups](shots/65.png) |
| `66` | Halloween | Seasonal | Halloween · 31 Oct | the cone becomes a witch's hat under a harvest moon. | [macOS](icons/macos/66.svg) · [iOS](icons/ios/66.svg) · [Android](icons/android/66.svg) · [Windows](icons/windows/66.svg) · [Linux](icons/linux/66.svg) · [mockups](shots/66.png) |
| `67` | Día de los Muertos | National | Día de Muertos · 1–2 Nov | papel picado, marigolds and a joyful magenta plate. | [macOS](icons/macos/67.svg) · [iOS](icons/ios/67.svg) · [Android](icons/android/67.svg) · [Windows](icons/windows/67.svg) · [Linux](icons/linux/67.svg) · [mockups](shots/67.png) |
| `68` | Thanksgiving | National | Thanksgiving · Nov | warm autumn plate with falling leaves around the cone. | [macOS](icons/macos/68.svg) · [iOS](icons/ios/68.svg) · [Android](icons/android/68.svg) · [Windows](icons/windows/68.svg) · [Linux](icons/linux/68.svg) · [mockups](shots/68.png) |
| `69` | Independence Day (US) | National | Fourth of July · 4 Jul | stars and stripes cone with fireworks over navy. | [macOS](icons/macos/69.svg) · [iOS](icons/ios/69.svg) · [Android](icons/android/69.svg) · [Windows](icons/windows/69.svg) · [Linux](icons/linux/69.svg) · [mockups](shots/69.png) |
| `70` | Fête nationale (FR) | National | 14 Juillet | bleu, blanc, rouge: a tricolore plate with a white cone and fireworks. | [macOS](icons/macos/70.svg) · [iOS](icons/ios/70.svg) · [Android](icons/android/70.svg) · [Windows](icons/windows/70.svg) · [Linux](icons/linux/70.svg) · [mockups](shots/70.png) |
| `71` | Oktoberfest | National | Oktoberfest · Sep–Oct, Munich | Bavarian lozenges, a pretzel and a blue-striped cone. | [macOS](icons/macos/71.svg) · [iOS](icons/ios/71.svg) · [Android](icons/android/71.svg) · [Windows](icons/windows/71.svg) · [Linux](icons/linux/71.svg) · [mockups](shots/71.png) |
| `72` | Carnaval (Rio) | National | Carnival · before Lent | a feathered cone in green, yellow and blue with confetti. | [macOS](icons/macos/72.svg) · [iOS](icons/ios/72.svg) · [Android](icons/android/72.svg) · [Windows](icons/windows/72.svg) · [Linux](icons/linux/72.svg) · [mockups](shots/72.png) |
| `73` | Pride | Seasonal | Pride Month · June | Progress-flag plate with a clean white cone. | [macOS](icons/macos/73.svg) · [iOS](icons/ios/73.svg) · [Android](icons/android/73.svg) · [Windows](icons/windows/73.svg) · [Linux](icons/linux/73.svg) · [mockups](shots/73.png) |
| `74` | King's Day (NL) | National | Koningsdag · 27 Apr | the Netherlands goes orange; the cone finally gets its crown. | [macOS](icons/macos/74.svg) · [iOS](icons/ios/74.svg) · [Android](icons/android/74.svg) · [Windows](icons/windows/74.svg) · [Linux](icons/linux/74.svg) · [mockups](shots/74.png) |
| `75` | Canada Day | National | Canada Day · 1 Jul | the flag's layout, with the cone standing in for the maple leaf. | [macOS](icons/macos/75.svg) · [iOS](icons/ios/75.svg) · [Android](icons/android/75.svg) · [Windows](icons/windows/75.svg) · [Linux](icons/linux/75.svg) · [mockups](shots/75.png) |
| `76` | Bonfire Night (UK) | National | Guy Fawkes Night · 5 Nov | sparkler trails and a bonfire glow. | [macOS](icons/macos/76.svg) · [iOS](icons/ios/76.svg) · [Android](icons/android/76.svg) · [Windows](icons/windows/76.svg) · [Linux](icons/linux/76.svg) · [mockups](shots/76.png) |
| `77` | Songkran | National | Songkran · 13–15 Apr, Thai New Year | water-splash turquoise and a freshly rinsed cone. | [macOS](icons/macos/77.svg) · [iOS](icons/ios/77.svg) · [Android](icons/android/77.svg) · [Windows](icons/windows/77.svg) · [Linux](icons/linux/77.svg) · [mockups](shots/77.png) |
| `78` | Nowruz | National | Nowruz · 20–21 Mar, Persian New Year | spring sabzeh sprouting around the cone. | [macOS](icons/macos/78.svg) · [iOS](icons/ios/78.svg) · [Android](icons/android/78.svg) · [Windows](icons/windows/78.svg) · [Linux](icons/linux/78.svg) · [mockups](shots/78.png) |
| `79` | Hanami | Seasonal | Hanami · cherry-blossom season, Japan | pale pink petals drifting past a pink-striped cone. | [macOS](icons/macos/79.svg) · [iOS](icons/ios/79.svg) · [Android](icons/android/79.svg) · [Windows](icons/windows/79.svg) · [Linux](icons/linux/79.svg) · [mockups](shots/79.png) |
| `80` | Santo António (Lisboa) | National | Santos Populares · 13 Jun, Lisbon | azulejo tiles, a grilled sardine and a festive cone. | [macOS](icons/macos/80.svg) · [iOS](icons/ios/80.svg) · [Android](icons/android/80.svg) · [Windows](icons/windows/80.svg) · [Linux](icons/linux/80.svg) · [mockups](shots/80.png) |
| `81` | Earth Day | Seasonal | Earth Day · 22 Apr | the cone standing on a small green-and-blue planet. | [macOS](icons/macos/81.svg) · [iOS](icons/ios/81.svg) · [Android](icons/android/81.svg) · [Windows](icons/windows/81.svg) · [Linux](icons/linux/81.svg) · [mockups](shots/81.png) |
| `82` | Mid-Autumn Festival | Seasonal | Mid-Autumn · 15th of the 8th lunar month | full moon, lantern and mooncake pattern. | [macOS](icons/macos/82.svg) · [iOS](icons/ios/82.svg) · [Android](icons/android/82.svg) · [Windows](icons/windows/82.svg) · [Linux](icons/linux/82.svg) · [mockups](shots/82.png) |
| `83` | Midsummer | Seasonal | Midsummer · late June, Nordics | midnight-sun sky and a flower crown around the cone. | [macOS](icons/macos/83.svg) · [iOS](icons/ios/83.svg) · [Android](icons/android/83.svg) · [Windows](icons/windows/83.svg) · [Linux](icons/linux/83.svg) · [mockups](shots/83.png) |

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

1. Every vote rewrites **[counts.json](https://paulfleury.com/vlc/counts.json)** on the live site: counts per concept, total votes, unique voters, a UTC timestamp and `ledger_sha256`, a hash of the private ballot file.
2. The private ballot file (`votes.private.php`) holds only pseudonymous hashes and is never served: a PHP guard line returns 404 and `.htaccess` denies it.
3. Snapshots of `counts.json` are committed to **[votes/counts.json](votes/counts.json)** with [`tools/sync-votes.sh`](tools/sync-votes.sh). The commit history is the ledger: anyone can diff two snapshots and see exactly how the count moved.

> [!WARNING]
> Votes are anonymous and unauthenticated. The voter ID is hashed together with the IP address, which makes ballot-stuffing harder but not impossible. Treat the tally as a signal, not a poll.

---

## 🚀 Deploy

**FTP or shared hosting (what runs [paulfleury.com/vlc](https://paulfleury.com/vlc/))**

1. Upload `index.html`, `icons.json`, `icons/`, `shots/`, `vote.php`, `.htaccess` and optionally `dump.zip` to one folder.
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
- **Page**: one file, vanilla JavaScript, no framework, no build step.

```
index.html          voting page and all dock mockups
icons.json          concept registry (id, name, family, description)
icons/<platform>/   100 SVGs per platform, plus raw layers
shots/              100 PNG mockup sheets
vote.php            PHP vote endpoint (FTP hosting)
votes/counts.json   committed snapshots of the public tally (the ledger)
api/votes.js        Vercel function (Vercel Blob)
server/server.py    standalone Python vote server
tools/              gen.py · shots.py · readme.py · sync-votes.sh
```

---

## 📄 License

Released under the [MIT License](LICENSE). "VLC" and the VLC cone are trademarks of VideoLAN; this is an independent design proposal.
