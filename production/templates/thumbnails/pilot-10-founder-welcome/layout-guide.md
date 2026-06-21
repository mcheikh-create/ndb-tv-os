# NDB-TV Pilot #10 — Thumbnail Layout Options

## Layout A: Founder-Left / Title-Right (Recommended)

```
┌──────────────────────────────────────────────┐
│                                              │
│  ┌──────────┐    ┌───────────────────┐       │
│  │          │    │                   │       │
│  │ FOUNDER  │    │   مرحباً بكم      │       │
│  │  PHOTO   │    │   في NDB-TV       │       │
│  │          │    │                   │       │
│  │          │    │   رؤيتنا          │       │
│  │          │    │   لنواذيبو        │       │
│  └──────────┘    └───────────────────┘  ┌────┐
│                                       │ LOGO│
│                                       └────┘
└──────────────────────────────────────────────┘
```

**Pros:**
- Natural reading flow (Arabic reads right-to-left — photo on left, text on right)
- Founder's face is visible and recognizable
- Title has dedicated space
- Logo sits cleanly in bottom-right corner

**Cons:**
- Founder photo must be well-framed for left-side placement
- Less space for title if photo is large

**Mobile readability:** Good — face + title are both visible

## Layout B: Logo-Top / Founder-Center / Title-Bottom

```
┌──────────────────────────────────────────────┐
│  ┌────┐                                       │
│  │LOGO│                                       │
│  └────┘                                       │
│                                              │
│         ┌──────────────┐                     │
│         │              │                     │
│         │   FOUNDER    │                     │
│         │    PHOTO     │                     │
│         │              │                     │
│         └──────────────┘                     │
│                                              │
│    ┌────────────────────────────┐            │
│    │   مرحباً بكم في NDB-TV     │            │
│    │   رؤيتنا لنواذيبو          │            │
│    └────────────────────────────┘            │
└──────────────────────────────────────────────┘
```

**Pros:**
- Symmetrical, balanced feel
- Title is prominent at the bottom (visible on most thumbnails)
- Founder centered (traditional portrait layout)

**Cons:**
- Logo at top competes with face for attention
- Vertical layout uses space less efficiently
- On very small displays, title at bottom may be cropped

**Mobile readability:** Moderate — title at bottom may be cut off on some surfaces

## Layout C: Title-Left / Founder-Right / Logo-Bottom

```
┌──────────────────────────────────────────────┐
│                                              │
│  ┌───────────────────┐  ┌──────────┐         │
│  │                   │  │          │         │
│  │   مرحباً بكم      │  │ FOUNDER  │         │
│  │   في NDB-TV       │  │  PHOTO   │         │
│  │                   │  │          │         │
│  │   رؤيتنا          │  │          │         │
│  │   لنواذيبو        │  │          │         │
│  └───────────────────┘  └──────────┘  ┌────┐│
│                                       │LOGO││
│                                       └────┘│
└──────────────────────────────────────────────┘
```

**Pros:**
- Arabic RTL reading — title is in the natural starting position
- Founder photo on right — less common, more distinctive
- Logo cleanly in corner

**Cons:**
- Text area is left of the photo — if Arabic text has diacritics it may crowd the photo
- Slightly unbalanced compared to Layout A

**Mobile readability:** Good — title visible in mobile feed center

---

## Comparison Table

| Criteria | Layout A | Layout B | Layout C |
|----------|----------|----------|----------|
| Arabic RTL reading flow | ✅ Natural | ⚠️ Neutral | ✅ Natural |
| Founder visibility | ✅ Good | ✅ Good | ✅ Good |
| Title visibility | ✅ Good | ⚠️ Risk at bottom | ✅ Good |
| Mobile readability | ✅ Best | ⚠️ Moderate | ✅ Good |
| Distinctiveness | ✅ Clean | ⚠️ Common | ✅ Distinctive |
| Logo placement | ✅ Corner | ⚠️ Top attention | ✅ Corner |
| Implementation ease | ✅ Easy | ✅ Easy | ✅ Easy |

---

## Recommendation

### Primary: Layout A — Founder-Left / Title-Right

**Reasoning:**

1. **Arabic natural reading flow** — Arabic reads right-to-left. The title starts on the right side where the eye naturally lands first, and the founder photo anchors the left side. A
2. **Title is most visible here** — placed in the center-right of the frame, it remains readable at all YouTube display sizes.
3. **Most YouTube thumbnails** use centered or left-aligned faces — this layout subtly differentiates while staying professional.
4. **Founder photo can be full frame** — head and shoulders, well-lit, natural expression.
5. **Logo fits cleanly** in the bottom-right corner without competing with any element.

### Implementation Guide for Layout A

| Element | Position | Size | Details |
|---------|----------|------|---------|
| Founder photo | Left half of frame (0,0 to 640,720) | ~640×720 | Head and shoulders. Founder looks slightly toward camera. Deep blue background behind. |
| Title (primary) | Right side, top-center (680, 160) | ~500×150 | "مرحباً بكم في NDB-TV" — 64px, Noto Sans Arabic Bold, White |
| Subtitle | Right side, below title (680, 340) | ~500×80 | "رؤيتنا لنواذيبو" — 32px, Noto Sans Arabic Regular, Light blue |
| Logo | Bottom-right (1120, 660) | ~140×140 | `assets/logo/youtube/youtube-profile-800x800.png` — scaled proportionally |

All positions are approximate and should be adjusted based on the actual founder photo framing and exact text width.
