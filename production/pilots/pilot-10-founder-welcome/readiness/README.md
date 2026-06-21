# NDB-TV Pilot #10 — Recording Readiness Packet

## What This Packet Controls

This packet is the final control layer before Pilot #10 recording begins. It brings together:

1. **Script approval** — Final sign-off on the Hassaniya script
2. **Channel readiness** — YouTube Studio shell is updated and ready
3. **Thumbnail readiness** — Design approved, founder photo needed
4. **Filming readiness** — Equipment, setup, and shot order
5. **Post-production plan** — Edit workflow, captions, private upload
6. **Publishing gate** — Final approval before going public

## Status

| Component | Status |
|-----------|--------|
| Script | Drafted in `script-hassaniya.md` — awaiting approval |
| Channel shell | Prepared in `studio-update-package/` — awaiting approval |
| Thumbnail | Design approved, placeholder ready — awaiting founder photo |
| Filming setup | Documented in `production-notes.md` — equipment check needed |
| Edit plan | Drafted in this packet |
| Publishing | Gated — final approval needed |

## Required Approvals Before Recording

| Gate | Item | Approved? |
|------|------|-----------|
| G1 | Script approved (tone, language, claims) | ☐ |
| G2 | Founder outfit and background confirmed | ☐ |
| G3 | Microphone and lighting tested | ☐ |
| G4 | Channel shell updates approved (but not yet applied) | ☐ |

## Required Approvals Before Publishing

| Gate | Item | Approved? |
|------|------|-----------|
| P1 | Final edited video reviewed by founder | ☐ |
| P2 | Thumbnail final PNG approved by founder | ☐ |
| P3 | Captions synced and correct | ☐ |
| P4 | Channel shell updated on YouTube | ☐ |
| P5 | Founder approves "publish now" | ☐ |

## Branch Structure

```
feature/pilot-10-recording-readiness   ← current
├── derives from feature/pilot-10-thumbnail
├── derives from feature/youtube-studio-update-package
│   └── derives from feature/youtube-channel-audit
│       └── derives from feature/pilot-10-founder-welcome
│           └── derives from feature/avatar-presenter-production-kit
│               └── main (689d986)
```

## Next Step

Founder reviews `script-approval-sheet.md`, `founder-recording-checklist.md`, and `final-publish-approval-sheet.md`. When these are signed, recording can begin.
