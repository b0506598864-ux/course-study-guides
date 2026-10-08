"""Conservative, auditable terminology normalization. Never rewrites original files."""
from pathlib import Path
import argparse
import hashlib
import json
import re
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument('--base', type=Path, required=True)
args = parser.parse_args()
base = args.base
repo = Path(__file__).resolve().parents[1]

# Long phrases run first. Ambiguous words such as יוזר, רף, רדיוס and ממו
# are deliberately NOT global replacements.
rules = [
    ('ריאקט ראוטר דום', 'react-router-dom'),
    ('בראוזר ראוטר', 'BrowserRouter'), ('פראוזר ראוטר', 'BrowserRouter'),
    ('בראוזר האוטר', 'BrowserRouter'),
    ('ראוטר פרוביידר', 'RouterProvider'),
    ('יוז לוקיישן', 'useLocation'), ('יוז נביגייט', 'useNavigate'),
    ('יוז קונטקסט', 'useContext'),
    ('יוז סטייט', 'useState'), ('יוסטייט', 'useState'), ('יו סטייט', 'useState'),
    ('you state', 'useState'),
    ('יוז אפקט', 'useEffect'), ('יוז פקט', 'useEffect'), ('יו זה פקט', 'useEffect'),
    ('יוז רף', 'useRef'), ('יוזרף', 'useRef'),
    ('יוז ממו', 'useMemo'), ('יוז מומו', 'useMemo'), ('יוזמו', 'useMemo'),
    ('יוזמנו', 'useMemo'),
    ('ממו איזיישן', 'memoization'), ('ממויזיישן', 'memoization'),
    ('ממוזיישן', 'memoization'), ('ממוזישן', 'memoization'),
    ('טייפ סקריפט', 'TypeScript'), ('טייפסקריפט', 'TypeScript'),
    ('ג׳אווה סקריפט', 'JavaScript'), ('גאווה סקריפט', 'JavaScript'),
    ("ג'אווה סקריפט", 'JavaScript'),
    ("ג'י אס איקס", 'JSX'), ('גי ס איקס', 'JSX'), ('טי אס איקס', 'TSX'),
    ('ג׳ייסון', 'JSON'), ('גייסון', 'JSON'),
    ('סטריקט מוד', 'StrictMode'), ('סטריקט מוט', 'StrictMode'),
    ('סייד אפקט', 'side effect'),
    ("און צ'יינג'", 'onChange'), ("און צ'ינג", 'onChange'),
    ("פייל לוד", 'payload'), ('פיילוד', 'payload'),
    ('אי פי איי', 'API'), ('אי פי אי', 'API'),
    ("לוקל סטורייג'", 'localStorage'), ('לוקל סטורייג', 'localStorage'),
    ("לוקאל סטורייג'", 'localStorage'), ('לוקאל סטורייג', 'localStorage'),
    ('רידקס', 'Redux'), ('רידאקס', 'Redux'), ('רדוקס', 'Redux'),
    ('רידיוסר', 'reducer'), ('רדיוסר', 'reducer'),
    ('ריאקט', 'React'), ('ראיאקט', 'React'),
    ('פרוביידר', 'Provider'), ('פרופס', 'props'),
    ('קומפוננטות', 'components'), ('קומפוננטס', 'components'),
    ('קומפוננטה', 'component'), ('קומפוננט', 'component'),
    ('סטייטים', 'states'), ('סטייטס', 'states'), ('סטייט', 'state'),
    ('קונטקסט', 'context'),
    ('ראוטינג', 'routing'), ('ראוטים', 'routes'),
    ('ראוטס', 'Routes'), ('ראוטר', 'router'), ('ראוט', 'Route'),
    ('הנדלר', 'handler'), ('אנדלר', 'handler'),
    ('דיספאץ', 'dispatch'),
    ('אינפוטים', 'inputs'), ('אינפוט', 'input'),
    ('ולידציה', 'validation'), ('וולידציה', 'validation'),
    ('ולידיישן', 'validation'), ('וולידיישן', 'validation'),
    ('וולידישן', 'validation'),
    ('רידמי', 'README'),
    ('הוקים', 'hooks'), ('הוק', 'hook'),
    ('ויט', 'Vite'),
    ('סטור', 'store'), ('לוקסטוריץ', 'localStorage'),
    ("לוק על סטורג'", 'localStorage'),
]
rules.sort(key=lambda pair: len(pair[0]), reverse=True)
compiled = [(old, new, re.compile(r'(?<![\w])([ובכלמשה]{0,2})' + re.escape(old) + r'(?![\w])')) for old, new in rules]
timing = re.compile(r'\d{2}:\d{2}:\d{2}[.,]\d{3} --> \d{2}:\d{2}:\d{2}[.,]\d{3}')

lessons = [
    ('2026-09-23', '2026-09-23-react', 'תמלול-מלא-large-v3/transcript.srt', 'srt'),
    ('2026-10-04', '2026-10-04-react-redux', '2026-10-04-verified-hebrew.vtt', 'vtt'),
    ('2026-10-07', '2026-10-07-react-forms', '2026-10-07-part-1-hebrew.vtt', 'vtt'),
    ('2026-10-07', '2026-10-07-react-forms', '2026-10-07-part-2-hebrew.vtt', 'vtt'),
]

def normalize(text, date):
    changes = []
    for old, new, pattern in compiled:
        # In the dogs transcript, "מייל ויט" describes weight, NOT the Vite tool.
        if old == 'ויט' and date != '2026-09-23':
            continue
        def replace(match):
            prefix = match.group(1)
            replacement = (prefix + '־' if prefix else '') + new
            changes.append({'before': match.group(0), 'after': replacement, 'term': new})
            return replacement
        text = pattern.sub(replace, text)
    return text, changes

for date, directory, filename, extension in lessons:
    part_two = '-part-2-' in filename
    source = base / directory / 'תמלול' / filename
    original_bytes = source.read_bytes()
    original = original_bytes.decode('utf-8-sig')
    source_times = timing.findall(original)
    output = []
    cues = []
    audit = []
    counts = Counter()
    # Cue boundaries and numbers stay untouched; only cue text is normalized.
    for block in re.split(r'\n\s*\n', original.replace('\r\n', '\n').strip()):
        match = timing.search(block)
        if not match:
            output.append(block)
            continue
        header, text = block[:match.end()], block[match.end():]
        corrected, edits = normalize(text, date)
        if part_two:
            for old, new in [('הייר אורדר פאנקשן', 'higher-order function'), ('בקאנד', 'backend')]:
                pattern = re.compile(r'(?<!\w)' + re.escape(old) + r'(?!\w)')
                count = len(pattern.findall(corrected))
                if count:
                    corrected = pattern.sub(new, corrected)
                    edits.extend([{'before': old, 'after': new, 'term': new}] * count)
        output.append(header + corrected)
        cues.append((match.group(0), corrected.strip()))
        if edits:
            audit.append({'timestamp': match.group(0), 'original': text.strip(), 'corrected': corrected.strip(), 'changes': edits})
            counts.update(edit['term'] for edit in edits)
    normalized = '\n\n'.join(output) + '\n'
    assert timing.findall(normalized) == source_times
    assert normalized.count('\ufffd') == original.count('\ufffd')
    shared = repo / 'transcripts' / ('L-' + date)
    local = base / directory / 'תמלול' / 'מתוקן-מונחים'
    if part_two:
        shared = shared / 'part-2'
        local = local / 'part-2'
    for destination in (shared, local):
        destination.mkdir(parents=True, exist_ok=True)
        (destination / f'{date}-terms-corrected.{extension}').write_text(normalized, encoding='utf-8-sig')
        (destination / f'{date}-terms-corrected.txt').write_text('\n\n'.join(t + '\n' + s for t, s in cues) + '\n', encoding='utf-8-sig')
        (destination / 'corrections.json').write_text(json.dumps({'date': date, 'source_sha256': hashlib.sha256(original_bytes).hexdigest(), 'source_cues': len(source_times), 'changed_cues': len(audit), 'replacements': sum(counts.values()), 'terms': dict(counts), 'audio_verified': False, 'changes': audit}, ensure_ascii=False, indent=2), encoding='utf-8')
    intro = f'# תמלול שיעור {date} עם מונחים באנגלית\n\n'
    intro += 'עותק לימודי של תמלול אוטומטי. תוקן כתיב של מונחים מזוהים; לא בוצעה הגהה מול האודיו. משפט לא ברור אינו הוראה מאומתת של המרצה. המקור נשמר מקומית ללא שינוי.\n\n'
    if date == '2026-10-04':
        intro += 'זהו הקובץ החדש שמתחיל ב־00:05:40, מן הקישור שאותר בנגן המסומן 04.10.2026. הוא שונה מהקובץ שהוצג כאן קודם.\n\n'
    if date == '2026-10-07' and not part_two:
        intro += 'זהו החלק הארוך שמתחיל ב־00:01:31. השיוך נתמך בקישור ההקלטה שנצפה ובתרגילי 7 באוקטובר בקוד המרצה. שיוכו הזמני ל־4 באוקטובר בוטל לאחר קבלת התמלול הנפרד של 4 באוקטובר. [המשך השיעור בן כ־13 דקות](part-2/README.md) נשמר בנפרד עם זמני הסרטון הקצר.\n\n'
    if part_two:
        intro += 'חלק ההמשך של 7 באוקטובר. הזמנים מתחילים מחדש ביחס לסרטון הקצר; לא נוספו להם ארבע שעות. [לחלק הראשון](../README.md).\n\n'
    intro += f'{len(cues):,} קטעים; {sum(counts.values()):,} החלפות מונחים. כל חותמות הזמן נשמרו.\n\n'
    intro += '[מילון התיקונים](TERMS.md) · [מקומות לבדיקה בהקלטה](NEEDS-AUDIO.md) · [יומן השינויים](corrections.json)\n\n'
    intro += f'[הורדת כתוביות](./{date}-terms-corrected.{extension}) · [קובץ טקסט](./{date}-terms-corrected.txt)\n\n'
    readable = intro + '\n\n'.join('**' + t + '**\n\n' + s for t, s in cues) + '\n'
    (shared / 'README.md').write_text(readable, encoding='utf-8')
    glossary = '# המונחים שתוקנו בתמלול\n\nהטבלה מציגה כתיב ולא הגדרה: מונח באנגלית אינו בהכרח פקודה או שם משתנה. שמות מתכנת ומילים כלליות לא הומרו למזהי קוד על סמך דמיון בלבד.\n\n| בתמלול המקורי | הכתיב באנגלית |\n|---|---|\n'
    glossary += '\n'.join(f'| {old} | `{new}` |' for old, new in rules if new in counts and any(old in a['original'] for a in audit)) + '\n'
    if part_two:
        glossary += '\n| הייר אורדר פאנקשן | `higher-order function` |\n| בקאנד | `backend` |\n'
    (shared / 'TERMS.md').write_text(glossary, encoding='utf-8')
    # Verify original file is untouched, timestamps and export encoding survive disk roundtrip.
    assert source.read_bytes() == original_bytes
    assert timing.findall((shared / f'{date}-terms-corrected.{extension}').read_text(encoding='utf-8-sig')) == source_times
    print(json.dumps({'date': date, 'cues': len(cues), 'changed_cues': len(audit), 'replacements': sum(counts.values()), 'terms': dict(counts)}, ensure_ascii=False))
