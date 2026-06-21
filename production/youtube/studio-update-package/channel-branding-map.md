# NDB-TV YouTube — Channel Branding Map

**Purpose:** Map every YouTube channel branding field to its corresponding repo asset.
**Status:** Draft — awaiting founder approval to apply.

---

## Field Map

| # | YouTube Field | Current State | Repo Asset | Classification | Action Required |
|---|--------------|--------------|------------|----------------|----------------|
| 1 | **Channel Name** | NDB-TV | N/A — brand name | ✅ **Match** | None |
| 2 | **Handle** | `@NDB-TV` | N/A — derived from name | ✅ **Match** | None |
| 3 | **Profile Picture** | Pre-v1.0 logo variant. 900×900 JPEG. Medium blue background (`RGB(0,70,158)`) with white NDB + red TV wordmark. No AI chip + open book emblem. | `assets/logo/youtube/youtube-profile-800x800.png` — Deep blue icon variant with emblem. 800×800 PNG. | ❌ **Inconsistent** | **MUST REPLACE** before any video. Upload repo asset as channel profile picture. |
| 4 | **Banner** | Exists but content unverified — CDN blocks direct inspection. 2560×424px max resolution. | `assets/logo/youtube/youtube-banner-2560x1440.png` — Full horizontal logo on deep blue. 2560×1440 PNG. | ❓ **Unknown match** | Visual verification required. Upload repo banner after approval. |
| 5 | **Watermark** | Not set | `assets/logo/video/lower-third-logo.png` (600×80) or icon variant. Can be used as YouTube brand watermark. | ❌ **Missing** | Optional — add after first video uploads. |
| 6 | **Video Watermark** | Not set | Same as above | ❌ **Missing** | Optional — YouTube can auto-add a channel logo to all videos. |
| 7 | **Intro Animation** | Not created in repo | `assets/logo/video/intro-logo.png` (1920×576) exists as static placeholder. Animated intro not yet produced. | ❌ **Missing** | Create animated intro as motion graphic. |
| 8 | **Outro End Screen** | Not created in repo | `assets/logo/video/outro-logo.png` (960×288) exists as static placeholder. Animated outro not yet produced. | ❌ **Missing** | Create animated end screen in YouTube Studio. |
| 9 | **Thumbnail Template** | Not created in repo | No template exists in `production/templates/thumbnails/` | ❌ **Missing** | Create before Pilot #10 (separate task). |
| 10 | **Channel Trailer** | Not set | N/A — no video exists | ❌ **Missing** | Optional — Pilot #10 can be set as channel trailer after publishing. |

---

## Upload Plan (After Founder Approval)

### Priority 1: Before Pilot #10 Publishes

| Order | Action | Source | Destination | Effort |
|-------|--------|--------|-------------|--------|
| 1 | Upload new profile picture | `assets/logo/youtube/youtube-profile-800x800.png` | YouTube Studio → Branding → Profile picture | 2 min |
| 2 | Upload new banner | `assets/logo/youtube/youtube-banner-2560x1440.png` | YouTube Studio → Branding → Banner image | 2 min |
| 3 | Update About section text | `about-section-draft.md` | YouTube Studio → Customization → About | 10 min |
| 4 | Set country to Mauritania | — | YouTube Studio → Settings → Channel → Country | 1 min |
| 5 | Add links | `links-and-contact-plan.md` | YouTube Studio → About → Links | 5 min |
| 6 | Update keywords | — | YouTube Studio → Settings → Channel → Keywords | 2 min |

**Total estimated effort: ~22 minutes**

### Priority 2: After Pilot #10 Publishes

| Order | Action | Source | Effort |
|-------|--------|--------|--------|
| 7 | Create Pilot #10 thumbnail | `production/templates/thumbnails/` (needs creation) | 1–2 hours |
| 8 | Upload Pilot #10 | Final MP4 | ~30 min (upload + processing) |
| 9 | Add watermark (optional) | `assets/logo/video/lower-third-logo.png` | 2 min |
| 10 | Set Pilot #10 as channel trailer | YouTube Studio → Branding → Channel trailer | 1 min |
| 11 | Create first playlists | See `channel-audit.md` section 5 | 5 min each |

### Priority 3: Later (Before Pilot #2)

| Order | Action | Effort |
|-------|--------|--------|
| 12 | Create animated intro | 2–4 hours (motion design) |
| 13 | Create animated end screen | 1–2 hours |
| 14 | Create thumbnail template | 1–2 hours |
| 15 | Configure upload defaults | 5 min |

---

## Visual Reference

Key visual identifiers for the brand match check:

- **Deep blue:** #0a1f3d / RGB(10, 31, 61) — field background
- **White:** #ffffff — "NDB" text
- **Red:** #e63946 — "TV" in wordmark
- **Emblem:** AI chip integrated with open book (left of wordmark)
- **Wordmark:** "NDB" white bold + "TV" red bold
- **Tagline (optional in banner):** "صوت المعرفة والابتكار في نواذيبو"
