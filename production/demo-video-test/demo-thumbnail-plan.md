# NDB-TV — Demo Thumbnail Plan

## Design

| Field | Value |
|-------|-------|
| **Size** | 1280 × 720 pixels |
| **Format** | PNG |
| **Background** | Deep blue `#0a1f3d` |
| **Title** | NDB-TV Test |
| **Subtitle** | Private Demo |
| **Logo** | NDB-TV icon (bottom-right) |
| **Human photo** | ❌ None — test only, no founder image needed |

## Layout

```
┌──────────────────────────────────────────────┐
│                                              │
│                                              │
│            NDB-TV Test                       │
│            Private Demo                      │
│                                              │
│                                              │
│                                        ┌────┐│
│                                        │LOGO││
│                                        └────┘│
└──────────────────────────────────────────────┘
```

- Title centered vertically and horizontally
- "NDB-TV Test" in large bold white text (64pt)
- "Private Demo" below in smaller light blue text (36pt)
- Logo bottom-right, ~130px
- No human photo, no clip art, no clickbait elements

## Text

| Element | Text | Font | Size | Color |
|---------|------|------|------|-------|
| Primary | NDB-TV Test | Noto Sans Arabic Bold | 64px | White `#ffffff` |
| Subtitle | Private Demo | Noto Sans Arabic Regular | 36px | Light blue `#4a7bb5` |

## Mobile Readability

- "NDB-TV Test" is 3 words — readable at 160×90
- High contrast white on deep blue
- Logo is recognizable even at small sizes

## Export

- PNG format
- 1280×720
- File name: `ndb-tv-private-demo-thumbnail.png`
- Saved to `production/demo-video-test/exports/`

## Notes

- This thumbnail is for the **private test video only**
- It clearly states "Test" and "Private Demo" — no public-facing claims
- If the demo is deleted after testing, this thumbnail can be deleted too
- Do not reuse this thumbnail for Pilot #10 or any public video
