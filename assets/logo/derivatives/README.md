# NDB-TV Derivative Asset Roadmap

**Source of Truth:** `assets/logo/master/ndb-tv-master-v1.png`

All derivative assets must be generated from the master PNG above. Do not redesign, reinterpret, or recreate the logo for any platform.

---

## Completed Derivatives

These assets have been generated and committed to the repository:

| Platform | File | Status |
|----------|------|--------|
| YouTube Profile | `assets/logo/youtube/youtube-profile-800x800.png` | ✅ Generated |
| YouTube Banner | `assets/logo/youtube/youtube-banner-2560x1440.png` | ✅ Generated |
| Facebook Profile | `assets/logo/social/facebook-profile.png` | ✅ Generated |
| WhatsApp Channel | `assets/logo/social/whatsapp-channel.png` | ✅ Generated |
| X/Twitter Profile | `assets/logo/social/x-profile.png` | ✅ Generated |
| Instagram Profile | `assets/logo/social/instagram-profile.png` | ✅ Generated |
| TikTok Profile | `assets/logo/social/tiktok-profile.png` | ✅ Generated |
| Telegram Channel | `assets/logo/social/telegram-profile.png` | ✅ Generated |
| Website Header | `assets/logo/social/website-header-1200x200.png` | ✅ Generated |
| Watermark (30%) | `assets/logo/print/ndb-tv-watermark.png` | ✅ Generated |
| Letterhead | `assets/logo/print/ndb-tv-letterhead.png` | ✅ Generated |
| Favicon 16px | `assets/logo/favicon/favicon-16.png` | ✅ Generated |
| Favicon 32px | `assets/logo/favicon/favicon-32.png` | ✅ Generated |
| Favicon 64px | `assets/logo/favicon/favicon-64.png` | ✅ Generated |
| Favicon ICO | `assets/logo/favicon/favicon.ico` | ✅ Generated |
| Intro Logo | `assets/logo/video/intro-logo.png` | ✅ Generated |
| Outro Logo | `assets/logo/video/outro-logo.png` | ✅ Generated |
| Lower-Third Overlay | `assets/logo/video/lower-third-logo.png` | ✅ Generated |

---

## Planned Derivatives

These assets require visual creative work (not just logo placement) and are planned for future production:

| Asset | Description | Priority | Dependencies |
|-------|-------------|----------|--------------|
| YouTube Banner (full) | Banner with tagline, channel name, and background design | HIGH | Tagline finalized |
| YouTube Channel Trailer | 30–60s intro video showcasing the channel | HIGH | Content strategy |
| Intro Animation (MP4) | 5-second animated logo reveal with audio | HIGH | Motion designer |
| Outro End Screen (MP4) | 10-second end screen with subscribe + recommended videos | HIGH | Intro animation template |
| Livestream Overlay Package | Full lower-thirds, side panels, transition graphics | MEDIUM | Intro animation settled |
| Thumbnail Templates | Branded PSD/SVG templates for consistent thumbnails | MEDIUM | Brand guidelines finalized |
| Business Card | Print-ready card with logo + contact | LOW | Contact details |
| Email Signature | HTML email signature with logo | LOW | Brand colors |
| NDB-TV Mobile App Icon | 1024×1024 for App Store + Google Play | FUTURE | App development |
| Social Media Cover Set | Facebook cover, X header, LinkedIn banner | LOW | Brand guidelines finalized |

---

## Regeneration

To regenerate all derivative PNGs from the master:

```bash
/home/mohiy/.hermes/hermes-agent/venv/bin/python3 \
  /home/mohiy/ndb-tv-os/scripts/generate-logos.py
```

This script reads `assets/logo/ndb-tv-logo-source.svg` and generates the master PNG + all derivatives. To add a new derivative, edit the script and rerun.

---

## Rules

1. **Always regenerate from master.** Never create a logo derivative from a previously generated derivative (quality degradation).
2. **Never crop the deep blue field.** The full logo field must always be visible.
3. **Color values are fixed.** Deep blue = `#0a1f3d`. Red accent = `#e63946`. White = `#ffffff`.
4. **The logo is frozen.** No redesigns, no reinterpretations. Version 1.0 is final.
