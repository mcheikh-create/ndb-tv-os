# NDB-TV — Demo Video Test Package

## Purpose

This package contains everything needed to produce and privately upload a short demo/test video for NDB-TV. The demo validates the production workflow — branding, export, captions, thumbnail, private upload, and review process — before Pilot #10 is recorded or published.

## Status

| Field | Value |
|-------|-------|
| **Status** | Internal test only — **not public** |
| **Not Pilot #10** | ❌ This is a separate test, not the first episode |
| **Branch** | `feature/demo-video-test-package` |
| **Expected use** | Private/unlisted upload workflow test |
| **Can go public?** | ❌ No — requires separate founder approval |

## What This Tests

1. Branding consistency (colors, logo placement)
2. Export quality (resolution, audio, encoding)
3. Caption sync (Arabic SRT)
4. Thumbnail rendering (design, mobile readability)
5. Private upload process (YouTube Studio)
6. Review workflow (founder sign-off on test results)
7. Identify production issues before Pilot #10

## Required Approvals

| Gate | Item | Status |
|------|------|--------|
| G1 | Founder approval to render actual demo video | ❌ Pending |
| G2 | Founder approval to upload privately to YouTube | ❌ Pending |
| G3 | Founder approval to share review link | ❌ Pending |
| G4 | Founder approval to convert private test to public | ❌ Not applicable — demo stays private |

## Package Contents

| File | Purpose |
|------|---------|
| `README.md` | This file |
| `demo-video-objective.md` | Demo goal and success criteria |
| `demo-script.md` | 30–45 second test script (Arabic) |
| `demo-shot-list.md` | Visual sequence |
| `demo-visual-plan.md` | Visual specifications |
| `demo-caption-plan.md` | Caption text and SRT plan |
| `demo-thumbnail-plan.md` | Demo thumbnail design |
| `private-upload-test-checklist.md` | Claude Chrome upload checklist |
| `review-scorecard.md` | Scoring rubric for demo review |
| `approval-gates.md` | Approval gate structure |
| `exports/` | Generated test media (optional) |

## Rendering Status

| Output | Status |
|--------|--------|
| Demo MP4 | ⏳ Pending founder approval to render |
| Demo thumbnail PNG | ⏳ Pending |
| Demo captions SRT | ⏳ Pending |
