# NDB-TV — Demo Caption Plan

## Caption Text

Full Arabic caption text matching `demo-script.md`:

```text
00:00:00,000 --> 00:00:03,000
السلام عليكم

00:00:03,000 --> 00:00:09,000
هذه رسالة اختبار خاصة لقناة NDB-TV

00:00:09,000 --> 00:00:17,000
هدفنا هو اختبار الصوت والصورة والترجمة وجودة الفيديو

00:00:17,000 --> 00:00:24,000
هذا الفيديو ليس برنامجًا حقيقيًا ولا يُنشر للجمهور

00:00:24,000 --> 00:00:30,000
شكرًا لمشاهدتكم — سنعود قريبًا ببرامجنا الأولى

00:00:30,000 --> 00:00:35,000
NDB-TV — اختبار خاص
```

## SRT File Format

The SRT file should be saved as `ndb-tv-private-demo-captions.srt` with:

- UTF-8 encoding (must support Arabic characters)
- LF line endings
- No BOM
- Sequential numbering (1–6 in this case)
- Proper timecode format: `hh:mm:ss,ms`

## Caption Styling Notes

- Arabic text renders correctly in YouTube's caption system
- White text with black outline (YouTube default) is acceptable
- Character limit per frame: 42 characters (2 lines max per subtitle)
- Reading speed: ~15–20 characters per second for Arabic
- Each subtitle frame should stay on screen 2–7 seconds

## French Caption Option (Optional)

```text
00:00:00,000 --> 00:00:03,000
Bonjour

00:00:03,000 --> 00:00:09,000
Ceci est un message de test privé pour NDB-TV

00:00:09,000 --> 00:00:17,000
Nous testons le son, l'image, les sous-titres et la qualité

00:00:17,000 --> 00:00:24,000
Cette vidéo n'est pas une émission réelle

00:00:24,000 --> 00:00:30,000
Merci d'avoir regardé

00:00:30,000 --> 00:00:35,000
NDB-TV — Test privé
```

## Caption Sync Checklist

| # | Check | Pass? |
|---|-------|-------|
| 1 | SRT file is UTF-8 encoded | ☐ |
| 2 | Arabic characters render correctly | ☐ |
| 3 | Timestamps align with spoken/narrated audio | ☐ |
| 4 | Each subtitle ≤ 42 characters | ☐ |
| 5 | Reading speed ≤ 20 chars/sec | ☐ |
| 6 | No overlapping timecode ranges | ☐ |
| 7 | Sequential numbering (1, 2, 3...) | ☐ |
| 8 | French SRT (optional) also verified | ☐ |

## Upload Notes

- YouTube supports SRT upload in video settings
- Upload as separate language track: Arabic (primary)
- French can be added as secondary language track
- Verify captions appear correctly in preview after upload
