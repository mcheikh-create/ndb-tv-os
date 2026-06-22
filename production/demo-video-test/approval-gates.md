# NDB-TV — Demo Video Approval Gates

**Status:** Pre-approval — no demo video rendered or uploaded yet.

---

## Gate Structure

```
Gate 1: Founder approves demo video rendering
    ↓
Gate 2: Founder approves private upload
    ↓
Gate 3: Founder reviews + approves test results
    ↓
Gate 4: Demo is deleted or retained as private reference
```

**Important:** The demo video cannot become public without a separate, explicit founder approval at a new gate.

---

## Gate 1: Approve Rendering

Before the demo MP4 is generated, the founder must approve:

| # | Item | Status |
|---|------|--------|
| 1.1 | Demo script reviewed and approved | ❌ Pending |
| 1.2 | Demo visual plan reviewed | ❌ Pending |
| 1.3 | Demo thumbnail design reviewed | ❌ Pending |
| 1.4 | Understanding confirmed: this is a test, not Pilot #10 | ❌ Pending |
| **Gate 1 Decision** | **☐ Proceed to render / ☐ Revise** | |

---

## Gate 2: Approve Private Upload

Before the demo is uploaded to YouTube, the founder must approve:

| # | Item | Status |
|---|------|--------|
| 2.1 | Demo video rendered and plays correctly | ❌ Pending |
| 2.2 | Captions SRT file created | ❌ Pending |
| 2.3 | Thumbnail PNG exported | ❌ Pending |
| 2.4 | Upload metadata correct (title, description, Private) | ❌ Pending |
| 2.5 | Claude Chrome has exact upload directive | ❌ Pending |
| **Gate 2 Decision** | **☐ Proceed to upload / ☐ Revise** | |

---

## Gate 3: Approve Test Results

After the demo is uploaded and reviewed, the founder must approve:

| # | Item | Status |
|---|------|--------|
| 3.1 | Review scorecard completed | ❌ Pending |
| 3.2 | All categories score ≥ 4 out of 5 | ❌ Pending |
| 3.3 | Any issues found are documented and fixable | ❌ Pending |
| 3.4 | Founder confirms: pipeline is ready for Pilot #10 | ❌ Pending |
| **Gate 3 Decision** | **☐ Ready for Pilot #10 / ☐ Fix issues first** | |

---

## Gate 4: Demo Retention

After testing is complete:

| # | Item | Status |
|---|------|--------|
| 4.1 | Demo video deleted from YouTube (if not needed) | ❌ Pending |
| 4.2 | Demo files retained in repo for reference | ❌ Pending |
| 4.3 | Demo thumbnail deleted (if unique and not reusable) | ❌ Pending |
| **Gate 4 Decision** | **☐ Keep / ☐ Delete** | |

---

## Critical Rule

> **The demo video is a private test. It cannot become public without a separate, explicit founder approval at a new gate.**
>
> This means:
> - No changing visibility from Private → Public
> - No using demo thumbnail for public videos
> - No reusing demo content in real episodes
> - No sharing demo link publicly (even as "behind the scenes")
>
> If the demo is deemed useful as public content, a new approval gate must be opened with updated script, thumbnail, and metadata.

---

## Additional Notes

- The demo may be deleted after Pilot #10 is published
- If the demo reveals technical issues (audio quality, encoding, captions), those are fixed in the Pilot #10 production files, not in the demo
- The demo is disposable by design
