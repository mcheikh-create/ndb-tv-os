# NDB-TV — Demo Video Objective

## Test Goal

Validate the NDB-TV production pipeline from script to private upload before Pilot #10 is committed. Identify and fix any issues with a low-stakes test.

## Success Criteria

| # | Criterion | How Measured |
|---|-----------|-------------|
| 1 | **Branding consistency** | Deep blue #0a1f3d background, NDB-TV logo present, no third-party branding |
| 2 | **Export quality** | 1920×1080, 30 fps, clean audio, no artifacts |
| 3 | **Caption sync** | Arabic SRT matches spoken audio, timing correct within ±0.5s |
| 4 | **Thumbnail rendering** | 1280×720 PNG, readable at mobile size, logo visible |
| 5 | **Private upload** | Successfully uploaded as Private/Unlisted with correct metadata |
| 6 | **Review process** | Founder can view private link and give feedback |
| 7 | **Issues identified** | Any problems found are documented for Pilot #10 fix |

## Non-Goals

- ❌ Not a real episode
- ❌ Not public-facing content
- ❌ Not an AI presenter test
- ❌ Not a audience engagement test
- ❌ Not a script or content quality test
- ❌ Not a replacement for Pilot #10

## Scope

- Internal workflow validation only
- Content is neutral placeholder text — no real information conveyed
- Video may be deleted after testing is complete
- All artifacts remain in repo for reference

## Deliverables for This Package

| Deliverable | Format | Notes |
|-------------|--------|-------|
| Demo script | Markdown | 30–45 seconds, neutral text |
| Demo visual plan | Markdown | 1920×1080, deep blue, logo |
| Demo captions | SRT + Markdown | Arabic, timecoded |
| Demo thumbnail | PNG | 1280×720, test title only |
| Demo video (optional) | MP4 | Generated if tools available |
| Upload checklist | Markdown | For Claude Chrome |
| Review scorecard | Markdown | Scoring rubric |
