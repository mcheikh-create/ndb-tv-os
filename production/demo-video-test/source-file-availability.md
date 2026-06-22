# NDB-TV — Demo Video Source File Availability

**Purpose:** Document where Claude Chrome can find the demo video files for private upload.
**Last Updated:** 2026-06-22

---

## Branch Information

| Field | Value |
|-------|-------|
| **Branch** | `feature/demo-video-test-package` |
| **Commit SHA** | `f99a5e84496bdf3b2e09e339d417472c3d400d8f` |
| **Remote URL** | https://github.com/mcheikh-create/ndb-tv-os/tree/feature/demo-video-test-package |
| **Pull request** | https://github.com/mcheikh-create/ndb-tv-os/pull/new/feature/demo-video-test-package |
| **Pushed to GitHub** | ✅ Yes |

---

## File Availability

### 1. Demo Video MP4

| Property | Value |
|----------|-------|
| **File** | `ndb-tv-private-demo-test.mp4` |
| **Size** | 190 KB |
| **Specs** | 1920×1080, 30fps, 35 seconds, H.264 |
| **Repo path** | `production/demo-video-test/exports/ndb-tv-private-demo-test.mp4` |
| **Raw URL** | https://raw.githubusercontent.com/mcheikh-create/ndb-tv-os/feature/demo-video-test-package/production/demo-video-test/exports/ndb-tv-private-demo-test.mp4 |
| **HTTP status** | ✅ 200 OK |

### 2. Demo Thumbnail PNG

| Property | Value |
|----------|-------|
| **File** | `ndb-tv-private-demo-thumbnail.png` |
| **Size** | 29 KB |
| **Specs** | 1280×720, deep blue bg, "NDB-TV Test / Private Demo" |
| **Repo path** | `production/demo-video-test/exports/ndb-tv-private-demo-thumbnail.png` |
| **Raw URL** | https://raw.githubusercontent.com/mcheikh-create/ndb-tv-os/feature/demo-video-test-package/production/demo-video-test/exports/ndb-tv-private-demo-thumbnail.png |
| **HTTP status** | ✅ 200 OK |

### 3. Demo Captions SRT

| Property | Value |
|----------|-------|
| **File** | `ndb-tv-private-demo-captions.srt` |
| **Size** | 590 B |
| **Format** | UTF-8 Arabic SRT, 6 entries, 35 seconds |
| **Repo path** | `production/demo-video-test/exports/ndb-tv-private-demo-captions.srt` |
| **Raw URL** | https://raw.githubusercontent.com/mcheikh-create/ndb-tv-os/feature/demo-video-test-package/production/demo-video-test/exports/ndb-tv-private-demo-captions.srt |
| **HTTP status** | ✅ 200 OK |

---

## Access Instructions for Claude Chrome

Claude Chrome should download the files from the raw GitHub URLs above, **not** from local file paths.

### Download Commands (if using terminal)

```bash
# Download MP4
curl -L -o ndb-tv-private-demo-test.mp4 \
  "https://raw.githubusercontent.com/mcheikh-create/ndb-tv-os/feature/demo-video-test-package/production/demo-video-test/exports/ndb-tv-private-demo-test.mp4"

# Download thumbnail
curl -L -o ndb-tv-private-demo-thumbnail.png \
  "https://raw.githubusercontent.com/mcheikh-create/ndb-tv-os/feature/demo-video-test-package/production/demo-video-test/exports/ndb-tv-private-demo-thumbnail.png"

# Download captions
curl -L -o ndb-tv-private-demo-captions.srt \
  "https://raw.githubusercontent.com/mcheikh-create/ndb-tv-os/feature/demo-video-test-package/production/demo-video-test/exports/ndb-tv-private-demo-captions.srt"
```

Alternatively, Claude Chrome can browse the branch at:
https://github.com/mcheikh-create/ndb-tv-os/tree/feature/demo-video-test-package/production/demo-video-test/exports/

And click "Raw" or "Download" for each file.

---

## Limitations

| Limitation | Note |
|------------|------|
| GitHub raw URLs have a 100 MB limit | Our MP4 is 190 KB — no issue |
| GitHub requires authentication for private repos | The repo `mcheikh-create/ndb-tv-os` is public — files are publicly accessible |
| Raw URLs return Content-Type headers | MP4 returns `application/octet-stream`, PNG returns `image/png`, SRT returns `text/plain` |

---

## Upload Instructions for Claude Chrome

These are documented in:
`production/demo-video-test/private-upload-test-checklist.md`

Key rules:
1. Upload as **Private** or **Unlisted** only
2. Title must include "PRIVATE TEST" or equivalent
3. Description must state "Internal test only"
4. Comments off
5. No public publishing
6. Do not add to any public playlist
