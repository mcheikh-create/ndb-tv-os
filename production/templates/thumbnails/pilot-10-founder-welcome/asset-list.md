# NDB-TV Pilot #10 — Thumbnail Assets List

## Required Assets

| # | Asset | Status | Source |
|---|-------|--------|--------|
| 1 | **Founder Photo** | ❌ **Not provided** — placeholder only. Founder must provide a real photo. | Founder |
| 2 | **NDB-TV Logo (icon variant)** | ✅ Available | `assets/logo/youtube/youtube-profile-800x800.png` |
| 3 | **Noto Sans Arabic font** | ✅ Downloadable (free) | Google Fonts — `NotoSansArabic[wdth,wght].ttf` |
| 4 | **Background color** | ✅ Defined | `#0a1f3d` — deep blue |
| 5 | **Background gradient/texture** | ⚠️ Optional | Simple gradient `#0a1f3d` → `#061526` if desired |

## Asset Details

### 1. Founder Photo

| Requirement | Specification |
|-------------|---------------|
| Format | JPEG or PNG |
| Resolution | Minimum 640×720 pixels (will be cropped to fit layout) |
| Framing | Head and shoulders, looking at camera |
| Expression | Warm, natural smile. Not serious or stern. |
| Lighting | Even light on face. No harsh shadows. |
| Background | Avoid busy backgrounds — plain or blurred is best |
| Clothing | Solid color preferred. Deep blue or neutral tones. |
| **Status** | **❌ Not yet provided — PLACEHOLDER will be used in draft** |

### 2. NDB-TV Logo

| Property | Value |
|----------|-------|
| Asset file | `assets/logo/youtube/youtube-profile-800x800.png` |
| Format | PNG (transparent background) |
| Size on thumbnail | ~140×140 pixels |
| Placement | Bottom-right corner |
| Note | This is the circular/icon variant. The full horizontal logo may also work but the icon variant is cleaner for corner placement. |

### 3. Noto Sans Arabic Font

| Property | Value |
|----------|-------|
| Font name | Noto Sans Arabic |
| Weight for title | Bold (700) |
| Weight for subtitle | Regular (400) |
| License | Open Font License (free for commercial use) |
| Download | `https://github.com/google/fonts/raw/main/ofl/notosansarabic/NotoSansArabic%5Bwdth%2Cwght%5D.ttf` |
| Fallback | Liberation Sans, DejaVu Sans (Arabic support is limited) |

### 4. Optional Assets

| Asset | When to Use | Notes |
|-------|-------------|-------|
| Nouadhibou skyline/photo | Only if rights-cleared. Adds local flavor. | Must be self-shot or CC-licensed. Do not use stock photos of unknown origin. |
| Subtle geometric pattern | If background feels flat | Use as overlay at < 5% opacity. Do not make it visible or distracting. |
| NDB-TV horizontal logo | Alternative to icon variant | `assets/logo/youtube/youtube-banner-2560x1440.png` scaled down. Test both. |

## Asset Preparation Workflow

1. Founder provides real photo
2. Photo is cropped to fit Layout A (640×720 left-aligned)
3. Color correction to match deep blue background
4. Logo placed at bottom-right
5. Text added in Noto Sans Arabic Bold
6. Final PNG exported at 1280×720

## Missing Assets Summary

| Missing Asset | Impact | Resolution |
|---------------|--------|------------|
| Founder photo | ❌ Cannot complete thumbnail | Founder must provide photo |
| Intro animation (not needed for thumbnail) | N/A | Separate task |
