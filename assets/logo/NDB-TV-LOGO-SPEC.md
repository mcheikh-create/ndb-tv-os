# NDB-TV Logo Specification

**Document Version:** 2.0
**Status:** Final — Approved
**Last Updated:** 2026-06-21

---

## 1. Logo Overview

The NDB-TV logo is a professional news-style wordmark that communicates trust, innovation, and local identity.

### Elements

1. **Background Field** — Deep blue rectangle (`#0a1f3d`), rounded corners (optional)
2. **"NDB"** — White bold text, left/upper portion
3. **"TV"** — Red bold text (`#e63946`), right/lower portion, same baseline as NDB
4. **Emblem** — AI microchip positioned above an open book, located above or beside the wordmark

### Meaning

| Element | Meaning |
|---------|---------|
| Deep blue field | Trust, professionalism, credibility |
| White "NDB" | Clarity, Nouadhibou identity, authority |
| Red "TV" | Energy, media, broadcast importance |
| AI chip | Artificial Intelligence — technology focus |
| Open book | Knowledge, education, learning |
| Chip + book together | AI-empowered education, knowledge in the AI era |

---

## 2. Color Specifications

### Primary Logo Colors

| Element | Color | HEX | RGB | CMYK | Pantone (Approx.) |
|---------|-------|-----|-----|------|-------------------|
| Background field | Deep Blue | `#0a1f3d` | `10, 31, 61` | `C:84 M:49 Y:0 K:76` | PMS 282 C |
| "NDB" text | White | `#ffffff` | `255, 255, 255` | `C:0 M:0 Y:0 K:0` | — |
| "TV" text | Red | `#e63946` | `230, 57, 70` | `C:0 M:75 Y:70 K:10` | PMS 186 C |
| Emblem icon | White | `#ffffff` | `255, 255, 255` | `C:0 M:0 Y:0 K:0` | — |
| Emblem detail | Red accent | `#e63946` | `230, 57, 70` | `C:0 M:75 Y:70 K:10` | PMS 186 C |

### Variant: Light Background Logo

For use on white or light-colored backgrounds (when the deep blue field cannot be used):

| Element | Color | HEX |
|---------|-------|-----|
| Background field | Dark Blue | `#0a1f3d` (same, always present) |
| "NDB" text | White | `#ffffff` |
| "TV" text | Red | `#e63946` |
| Emblem icon | White | `#ffffff` |

**Note:** The logo ALWAYS includes its deep blue background field. Never use individual elements without the field.

---

## 3. Geometry and Proportions

### Aspect Ratio

The primary logo maintains a **4:3** width-to-height ratio (horizontal layout).

### Proportion Guide

```
┌─────────────────────────────────────────────┐
│              DEEP BLUE FIELD                │
│                                             │
│             ┌──────┐                        │
│             │  AI  │                        │
│             │ CHIP │                        │
│             │ BOOK │                        │
│             └──────┘                        │
│          NDB         TV                     │
│                                             │
└─────────────────────────────────────────────┘

Not to scale — for spatial relationship reference only.
```

### Key Measurements

| Dimension | Value (relative to logo height) |
|-----------|--------------------------------|
| Logo height (H) | 1 unit |
| Logo width | ~2.5 units |
| Emblem height | 0.45 × H |
| Emblem width | 0.45 × H |
| Text height | 0.4 × H |
| NDB width | 0.8 × text area |
| TV width | 0.4 × text area |
| Gap between NDB and TV | 0.05 × text width |

### Clear Space

| Application | Minimum Clear Space |
|-------------|-------------------|
| Print | 1× logo height on all sides |
| Digital — standard | 1× logo height on all sides |
| Digital — constrained | 0.5× logo height minimum |
| Merchandise | 1.5× logo height on all sides |

---

## 4. Minimum Sizes

| Variant | Minimum Width | Minimum Height |
|---------|--------------|----------------|
| Primary (horizontal) | 120px | 48px |
| Icon-only | 48px | 48px |
| Print | 1.5 cm | 0.6 cm |

Below these sizes, use the icon-only variant.

---

## 5. File Formats

| Format | Use Case | Background |
|--------|----------|------------|
| PNG-24 | Digital — websites, social media, video | Deep blue field included |
| PNG-24 (transparent) | Video overlays, compositing | Transparent around field |
| SVG | Scalable — web, design tools | Deep blue field included |
| AI (Adobe Illustrator) | Source file — editing, derivatives | Editable layers |
| PDF | Print — documents, flyers, business cards | Deep blue field included |

---

## 6. Logo Variants

### Primary (Horizontal)
For most applications: channel banner, website header, video intro, social media banners.

*File: `ndb-tv-logo-primary.png`*

### Vertical (Stacked)
For vertical formats: YouTube Shorts, Instagram Stories, TikTok, mobile.

*File: `ndb-tv-logo-vertical.png`*

### Icon-Only (Emblem)
For small spaces: profile pictures, favicon, app icon, WhatsApp.

*File: `ndb-tv-logo-icon.png`*

### Monochrome (Black & White)
For single-color applications: fax, stamp, newspaper.

*File: `ndb-tv-logo-mono.png`*

---

## 7. Common Mistakes

| Mistake | Correct Approach |
|---------|------------------|
| Changing NDB to any color other than white | NDB is always white |
| Changing TV to any color other than red | TV is always `#e63946` red |
| Using logo without deep blue field | Logo always includes its field |
| Stretching logo to fit space | Maintain aspect ratio, resize proportionally |
| Adding drop shadows or effects | Use flat, clean logo only |
| Reversing NDB and TV positions | NDB left/above, TV right/below |
| Using low-resolution version | Always use appropriately sized file |
| Cropping the logo | Maintain full field and clear space |

---

## 8. Usage Scenarios

### YouTube Profile Image
- **Format:** Icon-only variant
- **Background:** Deep blue (`#0a1f3d`)
- **Size:** 800×800px
- **File:** `ndb-tv-logo-icon.png`

### YouTube Banner
- **Format:** Horizontal variant + tagline
- **Size:** 2560×1440px
- **Safe area (mobile):** 1546×423px centered
- **Safe area (tablet):** 1855×423px centered
- **File:** `ndb-tv-banner-youtube.png`

### Video Intro Animation
- **Format:** Primary logo animated
- **Duration:** 5 seconds
- **Resolution:** 1920×1080px
- **Build:** Icon animates in first → wordmark fades in below → tagline appears last
- **File:** `ndb-tv-intro-animation.mp4`

### Thumbnail Logo Overlay
- **Format:** Primary logo, reduced size
- **Position:** Bottom-right corner
- **Opacity:** 100%
- **Size:** 80–100px wide (on 1280×720px thumbnail)
- **Spacing:** 20px from bottom, 20px from right

### Livestream Overlay
- **Format:** Primary logo, semi-transparent
- **Position:** Bottom-right corner
- **Opacity:** 70%
- **Size:** 120–150px wide (on 1920×1080px stream)

### Website Header
- **Format:** Horizontal variant
- **Position:** Top-left of navigation
- **Size:** Proportional to header height (180–220px wide)

---

## 9. Design Files

All design source files are maintained in `assets/logo/`.

| File | Description |
|------|-------------|
| `ndb-tv-logo-primary.png` | Full color — deep blue field, white NDB, red TV |
| `ndb-tv-logo-primary-light.png` | Light variant for light backgrounds |
| `ndb-tv-logo-horizontal.png` | Horizontal layout |
| `ndb-tv-logo-vertical.png` | Vertical/stacked layout |
| `ndb-tv-logo-icon.png` | Icon-only - AI chip + book |
| `ndb-tv-logo-mono.png` | Monochrome variant |
| `ndb-tv-logo-source.ai` | Adobe Illustrator source |
| `ndb-tv-logo-source.svg` | SVG source |

---

## 10. Approval and Updates

- This specification is the single source of truth for the NDB-TV logo
- Any proposed change to the logo requires brand manager review
- Version history tracked in `docs/branding/CHANGELOG.md`
- All previous logo versions are deprecated

---

**Approved by:** NDB-TV Founding Team
**Effective Date:** 2026-06-21
**Supersedes:** All previous logo drafts and specifications
