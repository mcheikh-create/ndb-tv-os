# NDB-TV — Channel Operational Status

**Last Updated:** 2026-06-21
**Channel URL:** https://www.youtube.com/@NDB-TV
**Channel ID:** UCQKiM5mNIK4-W_sgI9qUdvw
**Branch:** `feature/channel-operational-governance`

---

## Current Live Channel State

| Field | Value | Status |
|-------|-------|--------|
| Channel name | NDB-TV | ✅ Set |
| Handle | @NDB-TV | ✅ Set |
| Videos | 0 | ✅ Empty channel |
| Playlists | 0 | ❌ Not created |
| Subscribers | 0 | ✅ Expected |
| Profile picture | Pre-v1.0 logo (blue/white/red) | ⏸️ Keep for now |
| Banner | Existing banner | ⏸️ Keep for now |
| About section | Bilingual, old tagline "صوت نواذيبو الجديدة" | ⏸️ Keep for now |
| Country | Morocco | ⏸️ Keep for now |
| Keywords | Set | ✅ Good |
| Contact links | None | ⏸️ None added |
| AI disclosure | Not in About section | ⏸️ Pending |

---

## Current Founder Decisions

| Decision | Ruling | Rationale |
|----------|--------|-----------|
| **Country** | Keep Morocco for now | Per founder directive — no change until after Pilot #10 |
| **Contact number** | Not added | Per founder directive — no phone/WhatsApp/email added at this stage |
| **Logo** | Keep current pre-v1.0 | Per founding directive — "Logos stay unchanged for now" |
| **Banner** | Keep current | Same |
| **About section** | Keep current text | Same — no edits until further notice |
| **Playlists** | Pending | Will create "Start Here" playlist later |
| **AI disclosure in channel** | Pending | Will add when script and channel are finalized |

---

## Pilot #10 Status

| Component | Status | File |
|-----------|--------|------|
| Script | Drafted — awaiting founder approval | `script-hassaniya.md` |
| Thumbnail | Placeholder PNG generated | `pilot-10-welcome-thumbnail.png` |
| Recording readiness | Packet prepared | `readiness/` |
| Channel shell | Prepared but paused | `studio-update-package/` |
| Recording | Not yet done | — |
| Private upload | Not yet done | — |
| Public publish | Not yet done | — |

---

## Readiness Score

**Current: 15/100**

Bottlenecks before score can increase:
- Script not yet approved by founder
- Channel shell changes not yet applied
- Thumbnail awaiting founder photo
- Recording not yet done

---

## Next Approved Repo-Side Tasks

| Priority | Task | Status |
|----------|------|--------|
| 1 | Founder reviews Pilot #10 script | ⏳ Pending |
| 2 | Founder approves script | ⏳ Pending |
| 3 | Recording equipment prepared per checklist | ⏳ Pending |
| 4 | Recording | ⏳ Pending |
| 5 | Captions + transcript preparation (Hermes) | ⏳ Pending |
| 6 | Channel shell update (founder decision) | ⏳ Pending |
| 7 | Private upload + founder review | ⏳ Pending |
| 8 | Final founder approval → publish | ⏳ Pending |

---

## Active Branches

| Branch | Purpose | Status |
|--------|---------|--------|
| `main` | Protected baseline (brand v1.0) | Protected |
| `feature/avatar-presenter-production-kit` | Avatar + presenter standards | Merged into Pilot #10 branches |
| `feature/pilot-10-founder-welcome` | Pilot #10 production package | Active |
| `feature/youtube-channel-audit` | Initial channel audit | Complete |
| `feature/youtube-studio-update-package` | Channel update preparation | Complete (actions paused) |
| `feature/pilot-10-thumbnail` | Thumbnail design | Complete |
| `feature/pilot-10-recording-readiness` | Recording readiness packet | Complete |
| `feature/youtube-minimum-channel-completion` | Claude Chrome handoff | Superseded |
| `feature/channel-operational-governance` | Current governance docs | **Active** |
