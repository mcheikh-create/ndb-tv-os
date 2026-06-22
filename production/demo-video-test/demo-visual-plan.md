# NDB-TV — Demo Visual Plan

## Technical Specifications

| Parameter | Value |
|-----------|-------|
| **Resolution** | 1920 × 1080 pixels |
| **Aspect Ratio** | 16:9 |
| **Frame Rate** | 30 fps |
| **Format** | MP4 (H.264) |
| **Bitrate** | 8–12 Mbps |
| **Audio** | AAC, 192 kbps (optional — silent version is acceptable) |
| **Duration** | 30–35 seconds |
| **Background Color** | `#0a1f3d` (deep blue) throughout |

## Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Deep Blue | `#0a1f3d` | Background |
| White | `#ffffff` | Title text, logo "NDB" |
| Red | `#e63946` | Logo "TV" |
| Light Blue | `#4a7bb5` | Subtitle/accent text |
| Dark Blue | `#061526` | Optional gradient bottom |

## Logo

| Use | Asset |
|-----|-------|
| Primary logo for demo | `assets/logo/youtube/youtube-profile-800x800.png` (icon variant) |
| Alternative | `assets/logo/master/ndb-tv-master-v1.png` (full master logo) |
| Placement | Centered on opening/closing cards, bottom-right on content slides |
| Size | ~200px wide for master logo, ~150px for icon variant |

## Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Title | Noto Sans Arabic | 52px | Bold | `#ffffff` |
| Body text | Noto Sans Arabic | 36px | Regular | `#ffffff` |
| Subtitle | Noto Sans Arabic | 28px | Regular | `#4a7bb5` |
| Disclosure | Noto Sans Arabic | 18px | Regular | `#4a7bb5` at 70% opacity |

## Audio

| Option | Description |
|--------|-------------|
| Silent | Simple test, no audio. Acceptable for caption timing test. |
| Voiceover | Founder reads demo script. Recorded on phone or directly. |
| AI voice | Only with disclosure. Avoid if possible for test simplicity. |
| Background music | Rights-free only. Must be CC0 or self-produced. Level at -25 dB. |

## Copyright

- ❌ No copyrighted music
- ❌ No unlicensed images
- ✅ Only NDB-TV brand assets (repo-owned)
- ✅ Only self-generated text content

## Rendering Tools

| Tool | Available | Notes |
|------|-----------|-------|
| FFmpeg | ✅ Yes | Can generate test pattern with text overlays |
| Pillow | ✅ Yes | Can generate image slides |
| DaVinci Resolve | ❌ Not available | Requires local install |
| CapCut | ❌ Not available | Requires local install |

If rendering, FFmpeg is the recommended tool for this demo — it produces a clean 1920×1080 H.264 MP4.
