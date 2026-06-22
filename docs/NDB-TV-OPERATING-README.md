# NDB-TV — Operating README

**GitHub:** `mcheikh-create/ndb-tv-os`
**YouTube:** https://www.youtube.com/@NDB-TV
**Last Updated:** 2026-06-21

---

## Mission

NDB-TV is a media and learning network built for Nouadhibou, Mauritania. It covers education, useful information, culture, youth skills, local stories, and community participation. Human presenters and clearly labeled AI presenters may both be used. Accuracy, respect, and community benefit are core rules.

**Tagline (Brand v1.0):** صوت المعرفة والابتكار في نواذيبو

---

## GitHub as Source of Truth

Everything about NDB-TV is documented here:

- Brand assets → `assets/logo/`
- Production plans → `production/`
- Strategy docs → `docs/strategy/`
- Templates → `production/templates/`
- Approval sheets → alongside their respective packages
- Audit reports → `production/youtube/`

Main branch is protected. Feature branches require review before merge.

---

## YouTube Channel

| Field | Value |
|-------|-------|
| URL | https://www.youtube.com/@NDB-TV |
| Status | Empty — no videos published |
| Shell | Minimal — logo, banner, About set (pre-v1.0) |
| Country | Morocco (kept for now per founder) |
| Next update | After Pilot #10 content is approved |

---

## Current Build Status

| Area | Status |
|------|--------|
| Brand v1.0 | ✅ Frozen at commit `689d986` |
| Avatar + presenter standards | ✅ Documented |
| Pilot #10 script | ✅ Drafted, awaiting founder approval |
| Pilot #10 thumbnail | ✅ Placeholder generated |
| Recording readiness | ✅ Packet prepared |
| Channel audit | ✅ Complete |
| Channel update package | ✅ Prepared but paused per founder |
| Recording | ❌ Not done |
| First publish | ❌ Not done |

---

## Active Branches

| Branch | Purpose |
|--------|---------|
| `main` | Protected baseline |
| `feature/pilot-10-founder-welcome` | Pilot #10 production files |
| `feature/channel-operational-governance` | Current governance docs |

See `production/youtube/channel-operational-status.md` for full branch list.

---

## Production Workflow

```
Founder intent
     ↓
ChatGPT (gatekeeper) → defines bounded work packet with allowed/forbidden scope
     ↓
Hermes (builder) → creates files, templates, documentation on feature branch
     ↓
Founder review and approval
     ↓
Claude Chrome (browser operator) → executes YouTube Studio changes from exact directives
     ↓
Founder final approval (if publishing)
```

---

## Role Split

| Role | Person/System | Responsibilities |
|------|---------------|------------------|
| **Founder** | Mohiyidine Cheikh | Final authority. Approves brand, content, publishing, partnerships. |
| **Gatekeeper** | ChatGPT | Converts intent to work packets. Defines scope. Reviews evidence. Prevents drift. |
| **Builder** | Hermes (this agent) | Creates repo files, production packets, templates, documentation. Maintains branch discipline. |
| **Browser Operator** | Claude Chrome | Makes YouTube Studio changes from exact directives when founder approves. |
| **Source of Truth** | GitHub (`mcheikh-create/ndb-tv-os`) | All decisions, approvals, and artifacts recorded in branches and commits. |

---

## Approval Gates

Founder approval is required before:

1. Changing public YouTube channel identity
2. Replacing logo or banner
3. Publishing any video
4. Using AI presenters publicly
5. Making claims about authority, partnerships, health, finance, or public institutions
6. Adding external links/contact points
7. Merging major branches into main
8. Launching promotional campaigns

---

## Pilot #10 Launch Sequence

```
Gate 1:  Script approval                       ← founder reviews script-hassaniya.md
Gate 2:  Recording                             ← founder records using readiness checklist
Gate 3:  Caption + transcript preparation       ← Hermes
Gate 4:  Channel shell update (if approved)     ← founder decides if/when
Gate 5:  Private upload + founder review        ← Claude Chrome or founder
Gate 6:  Final publish approval                 ← founder signs final-publish-approval-sheet.md
Gate 7:  Public publish
```

---

## What Is Paused

| Item | Reason |
|------|--------|
| Logo replacement | Founder decision: keep current for now |
| Banner replacement | Same |
| About section rewrite | Same |
| Country change | Same |
| Contact links | Same |
| AI disclosure in channel | Same |
| All live YouTube Studio changes | Per NDB-TV Build Governance Doctrine |

---

## What Is Next

| Step | What | Who |
|------|------|-----|
| 1 | Review Pilot #10 script | Founder |
| 2 | Approve or request edits | Founder |
| 3 | Record Pilot #10 | Founder |
| 4 | Prepare captions + transcript | Hermes |
| 5 | Channel shell decision | Founder |
| 6 | Upload + publish | Founder + Claude Chrome |
