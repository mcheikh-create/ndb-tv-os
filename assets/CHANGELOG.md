# Brand Asset Changelog

## 2026-06-21 — Version 1.0 — Founder-Approved Master Logo

### Summary
- Official PNG master logo adopted and designated as source of truth
- Brand identity frozen at v1.0 — no further redesigns
- Master asset designated as canonical visual reference
- All SVG files reclassified as supporting reference only

### Changelog
- Master PNG rendered at 4K (3840×1152) as the single source of truth
- All platform derivatives generated from master PNG
- Strict directory hierarchy established: master → youtube, social, print, video, favicon
- Logo hierarchy updated in documentation: SVG = supporting, PNG master = source of truth
- Generation script saved at `scripts/generate-logos.py`
- Directory structure settled: no more root-level logo files, organized by platform

### Files Added
- `assets/logo/master/ndb-tv-master-v1.png` — 4K master (source of truth)
- `assets/logo/master/ndb-tv-master-v1-2k.png` — 2K working copy
- `assets/logo/youtube/youtube-profile-800x800.png`
- `assets/logo/youtube/youtube-banner-2560x1440.png`
- `assets/logo/social/facebook-profile.png`
- `assets/logo/social/whatsapp-channel.png`
- `assets/logo/social/x-profile.png`
- `assets/logo/social/instagram-profile.png`
- `assets/logo/social/tiktok-profile.png`
- `assets/logo/social/telegram-profile.png`
- `assets/logo/social/website-header-1200x200.png`
- `assets/logo/print/ndb-tv-letterhead.png`
- `assets/logo/print/ndb-tv-watermark.png`
- `assets/logo/video/intro-logo.png`
- `assets/logo/video/outro-logo.png`
- `assets/logo/video/lower-third-logo.png`
- `assets/logo/favicon/favicon-16.png`
- `assets/logo/favicon/favicon-32.png`
- `assets/logo/favicon/favicon-64.png`
- `assets/logo/favicon/favicon.ico`
- `scripts/generate-logos.py`

### Files Modified
- `docs/branding/README.md` — Master hierarchy, updated file listing, new naming convention
- `assets/logo/NDB-TV-LOGO-SPEC.md` — Master source of truth declaration, updated design files table
