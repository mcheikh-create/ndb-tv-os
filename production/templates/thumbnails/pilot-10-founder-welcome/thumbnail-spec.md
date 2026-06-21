# NDB-TV Pilot #10 — Thumbnail Specification

## Technical Specifications

| Parameter | Value |
|-----------|-------|
| **Resolution** | 1280 × 720 pixels |
| **Aspect Ratio** | 16:9 |
| **Format** | PNG (lossless) |
| **Color Space** | sRGB |
| **Max File Size** | < 2 MB (YouTube recommends < 2 MB for PNG) |
| **Background Color** | `#0a1f3d` (deep blue — brand primary) |

## Safe Margins

YouTube displays thumbnails at various sizes. All critical content must stay within these margins:

| Platform | Safe Zone | Note |
|----------|-----------|------|
| Desktop (full) | Full 1280×720 | No cropping |
| YouTube home feed | ~480×270 display | Text must be readable |
| Mobile feed | ~160×90 display | **Only bold text visible** |
| Search results | ~246×138 display | Logo should be recognizable |
| Suggested videos sidebar | ~168×94 display | Minimal detail visible |

**Critical content safe zone:** Center 800×450 pixels (all key elements)
**Text safe zone:** Center 700×200 pixels (title only — must be bold)

## Design Elements

### 1. Background

- **Solid deep blue** `#0a1f3d` — fill entire 1280×720 canvas
- Optional subtle gradient: `#0a1f3d` (top) to `#061526` (bottom) — very subtle, not noisy
- Optional texture: none by default. If added, very low opacity geometric pattern only.

### 2. Logo Placement

- **Position:** Bottom-right corner
- **Asset:** `assets/logo/youtube/youtube-profile-800x800.png`
- **Size:** ~140px wide (scaled proportionally)
- **Spacing:** 20px from right edge, 20px from bottom edge
- **Opacity:** 100%

### 3. Founder Photo Placeholder

- **Position:** Left side or center (depends on layout — see `layout-guide.md`)
- **Size:** ~300–400px wide (head and shoulders)
- **Style:** Natural, warm, looking at camera. Casual professional.
- **Background of photo:** Should contrast against deep blue (e.g., lighter background behind person, or person framed with soft key light)
- **Note:** This is a **placeholder** — founder must provide a real photo

### 4. Title Text (Arabic)

- **Font:** Noto Sans Arabic, Bold weight
- **Color:** White (`#ffffff`)
- **Size:** 48–64px (depending on character count)
- **Position:** Right side or bottom (depends on layout)
- **Max words:** 4–5 words
- **Outline/shadow:** Very subtle dark shadow (#00000030, offset 1px) for readability on any background

### 5. Subtitle Text (Optional)

- **Font:** Noto Sans Arabic, Regular weight
- **Color:** Light blue or white at 80% opacity
- **Size:** 24–30px
- **Max words:** 3–4 words

## Mobile Readability Rules

| Rule | Reason |
|------|--------|
| Title must be readable when thumbnail is 160px wide | Mobile users see thumbnails at ~160×90 in feed |
| Use bold weight, large font | Thin or small text disappears on mobile |
| Avoid thin lines or small details | They blur at mobile sizes |
| Face should occupy ~30–40% of frame | So the person is recognizable at small sizes |
| No more than 5 words in title | Longer text becomes illegible on small screens |
| High contrast between text and background | White text on deep blue is ideal |

## Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Deep Blue | `#0a1f3d` | Background |
| White | `#ffffff` | Title text, "NDB" in logo |
| Red | `#e63946` | "TV" in logo |
| Light accent | `#4a7bb5` | Optional subtitle or divider |
| Dark accent | `#061526` | Optional gradient bottom |
| NDB-TV Logo | As provided in repo | Bottom-right placement |
