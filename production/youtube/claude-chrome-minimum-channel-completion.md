# Claude Chrome Handoff: Minimum NDB-TV Channel Completion

> **Hermes to Claude Chrome handoff.**
> Claude Chrome is the signed-in browser operator for YouTube Studio.
> Follow these exact directives. Do not expand scope.
> Founder has explicitly approved every action listed below.

---

## Objective

Make only the approved minimum YouTube Studio changes needed to make the NDB-TV channel operational for Pilot #10. No rebranding, no publishing, no deletions.

---

## Channel Identity

| Field | Value |
|-------|-------|
| **Channel Name** | NDB-TV |
| **Handle** | @NDB-TV |
| **Public URL** | https://www.youtube.com/@NDB-TV |
| **Channel ID** | UCQKiM5mNIK4-W_sgI9qUdvw |
| **Signed-In Account** | mohiyidinecheikh@gmail.com |

---

## Exact Actions (in order)

### A. Open YouTube Studio

Navigate to: **https://studio.youtube.com**

Sign in with the Google account above. If sign-in is blocked or requires verification, stop and report back — do not attempt workarounds.

### B. Confirm Correct Channel

Before making any changes, verify the channel header shows:
- **Channel:** NDB-TV
- **Handle:** @NDB-TV
- **Public URL** matches: https://www.youtube.com/@NDB-TV

If the channel is wrong (e.g., a different Google-brand account), stop and report.

### C. Set Country to Mauritania

1. In YouTube Studio, left menu → **Settings** → **Channel** → **Basic info**
2. Find the **Country** field
3. **If currently Morocco:** Change it to **Mauritania**
4. **If currently Mauritania already:** Leave unchanged, report as-is
5. **If country is something else entirely:** Change to Mauritania
6. Click **Save**

### D. Add Contact Number

The founder-approved contact number is: **+222 46 37 21 22**

YouTube Studio has two possible places for contact info:

#### D1. Links section (preferred)

- Left menu → **Customization** → **About**
- Find the **Links** section
- YouTube does NOT have a "phone number" link type — it only accepts URLs
- **If YouTube allows phone numbers as a link type:** Add `+222 46 37 21 22`
- **If only URLs are accepted:** Do NOT invent a WhatsApp URL. Do NOT add an incorrect link. Report the limitation.
- **If you know the correct WhatsApp URL format** (https://wa.me/22246372122): Do NOT add it unless you first pause and confirm with the founder. This handoff does not include WhatsApp URL approval.

#### D2. About description text (NOT approved)

Do NOT edit the About section text. The About section stays unchanged. If the phone number cannot be added as a link field, report the limitation — do not paste the number into the description body.

### E. Create "Start Here" Playlist

1. Left menu → **Playlists** → **New playlist** button
2. Title: `NDB-TV — Start Here`
3. If YouTube allows bilingual/alternate titles: Add Arabic subtitle `ابدأ من هنا`
4. **Visibility:**
   - If YouTube allows Public for an empty playlist: Choose **Public** (founder-approved — an empty public playlist is fine)
   - If only Private/Unlisted available: Choose **Private** and report
   - If YouTube requires a video to create a playlist: Cannot create — report the limitation
5. **Do not add any videos** — the playlist should remain empty
6. Click **Create**

### F. Verification

After completing C through E above, verify and confirm each item below. Navigate the live channel page (not Studio) to double-check visual state.

| # | Check | Result |
|---|-------|--------|
| 1 | Country is now Mauritania | ❓ |
| 2 | Contact number added successfully (or blocked with reason) | ❓ |
| 3 | "NDB-TV — Start Here" playlist exists | ❓ |
| 4 | Logo unchanged (still the pre-v1.0 blue logo) | ❓ |
| 5 | Banner unchanged | ❓ |
| 6 | About section unchanged | ❓ |
| 7 | No videos uploaded (0 videos) | ❓ |
| 8 | No publish action taken | ❓ |
| 9 | No deletions performed | ❓ |
| 10 | Channel handle still @NDB-TV | ❓ |
| 11 | Channel name still NDB-TV | ❓ |
| 12 | Ownership/permissions unchanged | ❓ |

---

## Strict Forbidden Actions

| ❌ Must NOT Do | Rationale |
|---------------|-----------|
| Change logo | Not founder-approved per NDB-TV Build Governance Doctrine |
| Change banner | Not founder-approved |
| Rewrite About section | Not founder-approved (even adding phone to description) |
| Upload any video | Pilot #10 not yet recorded or approved |
| Publish content | Final publish requires separate founder approval sheet sign-off |
| Delete anything | No content exists to delete, but don't touch |
| Change monetization | Not founder-approved |
| Change ownership or permissions | Not founder-approved |
| Change handle (@NDB-TV) | Not founder-approved |
| Add unapproved websites/social links | Only the phone number is approved; no Facebook, Instagram, or website |
| Invent WhatsApp URL | Must pause and ask founder before adding WhatsApp link |
| Claim authority/funding/partnerships | Per NDB-TV brand rules |
| Merge to main | Per repo rules |

---

## If Anything Goes Wrong

If YouTube asks for:
- Phone verification / 2FA
- Re-authentication
- CAPTCHA
- Any unfamiliar prompt

**Stop immediately.** Do not click through. Report what the prompt says back to Hermes/ChatGPT.

---

## Expected Final Report from Claude Chrome

Complete this section after executing:

```
## Country Change
[Result: Mauritania set / Already Mauritania / Blocked — reason]

## Contact Number
[Result: Added as link / Cannot add — limitation / Blocked — reason]

## Playlist
[Result: Created — "NDB-TV — Start Here" (Public/Private) / Cannot create — reason]

## Screenshots/Confirmation Notes
[Brief description of what you saw on screen confirming each change]

## Blocked Items
[List anything that could not be done]

## Logo/Banner/About Confirmation
[Confirmed unchanged — how you verified]

## No Upload/Publish Confirmation
[Confirmed no accidental upload or publish]

## Updated Operational Readiness Score
[Score before: 15/100 → Score now: X/100]
```

---

## Branch Note for Hermes

After Claude Chrome completes and reports, Hermes should:

1. Create `production/youtube/live-minimum-channel-completion-report.md` with Claude Chrome's results
2. Commit on branch `feature/youtube-minimum-channel-completion-report`
3. Message: `youtube: document minimum live channel completion`
4. Do not push to main
