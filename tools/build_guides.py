from pathlib import Path
import shutil


COURSE_ROOT = Path(r"C:\Users\B0506.DESKTOP-7JV0N2N\Desktop\לימודים FULLSTACK\הקלטות")
REPO_ROOT = COURSE_ROOT / "course-study-guides"
GUIDES = REPO_ROOT / "guides"
LESSON_GUIDES = GUIDES / "lessons"
TRANSCRIPTS = REPO_ROOT / "transcripts"


def ex(code, folder, title, purpose, syntax=""):
    return {
        "code": code,
        "folder": folder,
        "title": title,
        "purpose": purpose,
        "syntax": syntax,
    }


def hw(code, filename, summary):
    return {"code": code, "filename": filename, "summary": summary}


def rule(code, priority, text, source, timestamp, related=""):
    return {
        "code": code,
        "priority": priority,
        "text": text,
        "source": source,
        "timestamp": timestamp,
        "related": related,
    }


lessons = [
    {
        "id": "L-2026-06-24",
        "folder": "HTML & CSS - 24-06-2026",
        "title": "HTML ו-CSS - תחילת הקורס",
        "source_status": "תיקיות התמלול ושיעורי הבית קיימות אך ריקות. אין מקור שמאפשר סיכום ודאי.",
        "learned": ["אין חומר מקומי מאומת לשיעור זה."],
        "syntax": [],
        "exercises": [],
        "homework": [],
        "rules": [],
    },
    {
        "id": "L-2026-06-28",
        "folder": "HTML & CSS - 28-06-2026",
        "title": "HTML - בניית אתרי תוכן",
        "source_status": "אין תמלול או קוד כיתה; הסיכום מבוסס על חמש משימות Word.",
        "learned": [
            "בניית אתר HTML בנושא מוגדר.",
            "חלוקת תוכן לכותרות, פסקאות, קישורים, רשימות ותמונות.",
            "תרגול אותו מבנה במספר עולמות תוכן: ספורט, גינון, ספרים, תכנות ואתר אישי.",
        ],
        "syntax": ["<!DOCTYPE html>", "html", "head", "body", "h1-h6", "p", "a", "img", "ul/ol/li"],
        "exercises": [],
        "homework": [
            hw("HW01", "01 - HTML - Sports Website.docx", "בניית אתר תוכן בנושא ספורט."),
            hw("HW02", "02 - HTML - Gardening Website.docx", "בניית אתר תוכן בנושא גינון."),
            hw("HW03", "03 - HTML - My Website.docx", "בניית אתר אישי."),
            hw("HW04", "04 - HTML - Books Website.docx", "בניית אתר בנושא ספרים."),
            hw("HW05", "05 - HTML - Software Programming Website.docx", "בניית אתר בנושא תכנות."),
        ],
        "rules": [],
    },
    {
        "id": "L-2026-07-01",
        "folder": "HTML & CSS - 01-07-2026",
        "title": "HTML ו-CSS",
        "source_status": "תיקיות התמלול ושיעורי הבית קיימות אך ריקות. אין מקור שמאפשר סיכום ודאי.",
        "learned": ["אין חומר מקומי מאומת לשיעור זה."],
        "syntax": [],
        "exercises": [],
        "homework": [],
        "rules": [],
    },
    {
        "id": "L-2026-07-05",
        "folder": "JavaScript Basics - 05-07-2026",
        "title": "CSS - עיצוב אתרים קיימים",
        "source_status": "אין תמלול או קוד כיתה; הסיכום מבוסס על משימות Word.",
        "learned": [
            "חיבור קובץ CSS ל-HTML.",
            "עיצוב דפים שכבר נבנו.",
            "שימוש ב-selectors, צבעים, גדלים, מרווחים וגבולות.",
        ],
        "syntax": ["<link rel=\"stylesheet\">", "selector { property: value; }", ".class", "#id"],
        "exercises": [],
        "homework": [
            hw("HW01", "01 - HTML & CSS - Previuos Websites Design.docx", "עיצוב אתרי ה-HTML הקודמים."),
            hw("HW02", "02 - HTML & CSS - Design Existing HTML Page.docx", "קבלת דף קיים ושיפור המראה שלו."),
            hw("HW03", "03 - HTML & CSS - Animal Store Website.docx", "בניית ועיצוב אתר חנות חיות."),
        ],
        "rules": [],
    },
    {
        "id": "L-2026-07-08",
        "folder": "JavaScript Basics - 08-07-2026",
        "title": "CSS Flex ו-Grid",
        "source_status": "אין תמלול או קוד כיתה; הסיכום מבוסס על שתי משימות Word.",
        "learned": ["סידור רכיבים בעזרת Flexbox.", "סידור רכיבים דו-ממדי בעזרת CSS Grid.", "הבנת container וילדים."],
        "syntax": ["display: flex", "justify-content", "align-items", "gap", "display: grid", "grid-template-columns"],
        "exercises": [],
        "homework": [
            hw("HW01", "Copy of 04 - CSS - Flex & Grid.docx", "תרגול פריסות Flex ו-Grid."),
            hw("HW02", "Copy of 05 - CSS - Flex & Grid.docx", "תרגול נוסף של פריסות Flex ו-Grid."),
        ],
        "rules": [],
    },
    {
        "id": "L-2026-07-12",
        "folder": "JavaScript Basics - 12-07-2026",
        "title": "JavaScript - משתנים וערכים",
        "source_status": "אין תמלול או קוד כיתה; הסיכום מבוסס על שיעורי הבית.",
        "learned": ["יצירת משתנים.", "הכנסת ערכים למשתנים.", "מספרים, מחרוזות וערכים בוליאניים.", "הצגה וחישובים בסיסיים."],
        "syntax": ["const", "let", "=", "+ - * /", "string", "number", "boolean", "document.write", "console.log"],
        "exercises": [],
        "homework": [hw("HW01", "01 - JavaScript - Variables.docx", "תרגול יצירה, השמה ושימוש במשתנים.")],
        "rules": [],
    },
    {
        "id": "L-2026-07-15",
        "folder": "JavaScript Basics - 15-07-2026",
        "title": "JavaScript Basics",
        "source_status": "קיימים קטעי תמלול קצרים מאוד ללא מספיק הקשר; אין שיעורי בית או קוד כיתה.",
        "learned": ["אין מספיק חומר מקומי כדי לקבוע בוודאות את תוכן השיעור."],
        "syntax": [],
        "exercises": [],
        "homework": [],
        "rules": [],
    },
    {
        "id": "L-2026-07-19",
        "folder": "JavaScript Basics - 19-07-2026",
        "title": "לולאות ולולאות מקוננות",
        "source_status": "הסיכום מבוסס על שיעורי הבית. שמות קובצי התמלול אינם תואמים לתאריך ולכן לא סווגו מהם כללי מרצה.",
        "learned": ["חזרה על פעולה באמצעות לולאה.", "מונה, תנאי עצירה והתקדמות.", "לולאה בתוך לולאה לצורות, טבלאות ומטריצות."],
        "syntax": ["for", "while", "do...while", "break", "continue", "i++", "nested loop"],
        "exercises": [],
        "homework": [
            hw("HW01", "01 - JavaScript - Loops.docx", "תרגול לולאות, רצפים וחזרות."),
            hw("HW02", "02 - Nested Loops.docx", "תרגול לולאות מקוננות וצורות."),
        ],
        "rules": [],
    },
    {
        "id": "L-2026-07-26",
        "folder": "JavaScript Basics - 26-07-2026",
        "title": "מערכים, אובייקטים ומערך אובייקטים",
        "source_status": "התמלול קצר וחלקי; הסיכום מבוסס בעיקר על שלוש משימות Word.",
        "learned": [
            "מערך הוא רשימה מסודרת עם אינדקסים שמתחילים ב-0.",
            "אובייקט מרכז מאפיינים של ישות אחת.",
            "מערך אובייקטים משמש לשמירת רשימה של ישויות.",
            "מעבר על properties באמצעות for-in ועל רשימה באמצעות לולאה.",
        ],
        "syntax": ["[]", "{}", "array[index]", "object.property", "push", "length", "for...in"],
        "exercises": [],
        "homework": [
            hw("HW01", "01 - Arrays.docx", "יצירה, מילוי ומעבר על מערכים."),
            hw("HW02", "02 - Objects.docx", "יצירת אובייקטים והצגת מאפיינים, כולל for-in כאתגר."),
            hw("HW03", "03 - Array of Objects.docx", "מכוניות, בגדים ו-Geolocation כמערכי אובייקטים."),
        ],
        "rules": [],
    },
    {
        "id": "L-2026-07-29",
        "folder": "JavaScript Basics - 29-07-2026",
        "title": "פונקציות ו-return",
        "source_status": "קיימים תמלולים ושתי משימות Word. הסיכום נשען בעיקר על נוסח המשימות.",
        "learned": [
            "הגדרת פונקציה וקריאה לפונקציה.",
            "parameters הם שמות שהפונקציה מקבלת; arguments הם הערכים שנשלחים בקריאה.",
            "פונקציה יכולה להציג מידע או להחזיר תוצאה באמצעות return.",
            "חלוקת בעיה גדולה לפונקציות קטנות ושימוש חוזר.",
        ],
        "syntax": ["function name(parameters) { }", "name(arguments)", "return", "Math.random", "Date"],
        "exercises": [],
        "homework": [
            hw("HW01", "02 - Functions.docx", "פונקציות להצגה, חישובים, סמיילים, זמן, מערכים וצורות."),
            hw("HW02", "03 - Function Return Value.docx", "פונקציות שמחזירות ממוצע, מינימום, boolean, אובייקט או מערך."),
        ],
        "rules": [
            rule("TR01", "PREFERRED", "שם פונקציה צריך לתאר את הפעולה שלה; get מתאים לפונקציה שמחזירה ערך ולא רק מציגה.", "02-transcript-with-timestamps.txt", "57:57-58:03", "Functions"),
            rule("TR02", "MUST UNDERSTAND", "יש להבדיל בין הפונקציה עצמה לבין invocation: שם בלבד הוא הפונקציה; שם עם () מפעיל אותה.", "02-transcript-with-timestamps.txt", "43:31-43:50; 02:49:35-02:49:42", "Functions"),
            rule("TR03", "PREFERRED", "פונקציות קטנות מונעות חזרה ומקדמות DRY - Don't Repeat Yourself.", "02-transcript-with-timestamps.txt", "41:07-41:19", "Functions"),
        ],
    },
    {
        "id": "L-2026-08-02",
        "folder": "JavaScript & HTML - 02-08-2026",
        "title": "Strings, JSON ופונקציות שימושיות",
        "source_status": "קיימים שני חלקי תמלול ושתי משימות Word.",
        "learned": [
            "פונקציות של מחרוזות: includes, substring ו-trim.",
            "JSON כפורמט להעברת מידע בין מערכות.",
            "פונקציות בוליאניות ושימוש חוזר בפונקציות.",
            "הבדל בין ערכים פרימיטיביים לבין אובייקטים ומערכים.",
        ],
        "syntax": ["includes", "substring", "trim", "length", "JSON.stringify", "JSON.parse", "typeof", "===", "truthy/falsy"],
        "exercises": [],
        "homework": [
            hw("HW01", "02 - JSON.docx", "תרגול יצירה וקריאה של מבני JSON."),
            hw("HW02", "03 - Strings.docx", "תרגול מתודות וחישובים על מחרוזות."),
        ],
        "rules": [
            rule("TR01", "PREFERRED", "כדי לבדוק אם מחרוזת נמצאת במחרוזת אחרת, להשתמש ב-includes; אין צורך לזכור את השיטה ההיסטורית.", "01-transcript-with-timestamps.txt", "15:01-15:09", "Strings"),
            rule("TR02", "MUST UNDERSTAND", "שמות משתנים המתכנת בוחר; שמות הפונקציות וה-Syntax של JavaScript הם הדברים שצריך לזהות.", "01-transcript-with-timestamps.txt", "19:27-20:02", "Syntax vocabulary"),
            rule("TR03", "MUST UNDERSTAND", "JSON חשוב כי כמעט כל תקשורת בין אפליקציות משתמשת בו.", "02-transcript-with-timestamps.txt", "32:43-32:50", "JSON"),
            rule("TR04", "MUST UNDERSTAND", "empty string ו-undefined הם falsy.", "02-transcript-with-timestamps.txt", "03:58:46 ואילך", "Truthy/Falsy"),
        ],
    },
    {
        "id": "L-2026-08-05",
        "folder": "הנחיית פרויקט - HTML , CSS , J - 05-08-2026",
        "title": "DOM, Events ו-Dynamic HTML",
        "source_status": "קיימים תמלולים עם timestamps ושיעורי בית DOM.",
        "learned": [
            "ה-DOM הוא המבנה שהדפדפן בונה מה-HTML.",
            "איתור אלמנטים ושינוי properties, style ו-classes.",
            "אירועים ב-HTML מפעילים פונקציות JavaScript.",
            "יצירת HTML דינמי באמצעות innerHTML ו-template literals.",
        ],
        "syntax": ["document.getElementById", "querySelector", "querySelectorAll", ".value", ".style", ".classList.add", "event", "innerHTML", "backticks", "${}"],
        "exercises": [],
        "homework": [hw("HW01", "01 - DOM.docx", "טפסים, alert/span, שינוי צבע, אירועי עכבר ומקלדת.")],
        "rules": [
            rule("TR01", "MUST NOT", "בקורס לא להשתמש ב-querySelector כדרך הראשית; לחפש id מתאים ולעבוד עם getElementById.", "project transcript with timestamps", "03:00:34-03:00:47", "DOM selection"),
            rule("TR02", "PREFERRED", "שינויי מראה עדיף להגדיר ב-CSS ולהוסיף/להסיר class ב-JavaScript.", "project transcript with timestamps", "03:27:47-03:28:00", "CSS/DOM"),
            rule("TR03", "MUST", "בתוך form לעבוד עם onsubmit ולא עם onclick של כפתור השליחה.", "part-3 transcript with timestamps", "15:50-17:08", "Forms"),
            rule("TR04", "PREFERRED", "כאשר רצים על מערך להשתמש ב-for...of ולא ב-for רגילה; for רגילה נשמרת למצב שאין מערך לרוץ עליו.", "project transcript with timestamps", "03:44:20-03:44:55", "Loops"),
            rule("TR05", "PREFERRED", "Dynamic HTML: הנתונים מגיעים ל-JavaScript והוא מסנכרן אותם ל-DOM באמצעות innerHTML.", "project transcript with timestamps", "03:46:02-03:46:15", "Dynamic HTML"),
        ],
    },
    {
        "id": "L-2026-08-09",
        "folder": "הנחיית פרויקט - HTML , CSS , J - 09-08-2026",
        "title": "טופס, Validation, DHTML, מחיקה ו-Local Storage",
        "source_status": "זהו מקור מרכזי למבחן. קיימים תמלולים, 12 תרגילים, קובץ הכנה למבחן ומיפוי מפורט קיים.",
        "learned": [
            "Form -> onsubmit -> preventDefault -> קריאת value.",
            "Validation בסיסי ב-HTML ומורכב ב-JavaScript.",
            "יצירת שורות בטבלה באמצעות innerHTML, backticks ו-${}.",
            "מערך אובייקטים, Local Storage ו-JSON.",
            "SSOT: המידע ב-Storage וה-DOM הוא תצוגה בלבד.",
            "מחיקה לפי index, splice, save ו-sync.",
        ],
        "syntax": ["required", "min/max", "minlength/maxlength", "event.preventDefault", "getElementById(...).value", "innerHTML", "localStorage", "JSON.stringify/parse", "push", "splice", "confirm", "for...of"],
        "exercises": [
            ex("E01", "01-homework-6", "אירועי עכבר ו-class", "שינוי class לפי id.", "mouseenter, mouseleave, classList"),
            ex("E02", "01-homework-6-dynamic", "event.target", "אותה פעולה בלי להעביר id.", "event.target"),
            ex("E03", "03-collect-user-date-from-form", "טופס לטבלה", "קריאת טופס והוספת שורה דינמית.", "onsubmit, preventDefault, value, innerHTML"),
            ex("E04", "04-color-input-change-row-color", "צבע דינמי", "הכנסת צבע מהטופס ל-style של השורה."),
            ex("E05", "05-image-url-input", "תמונה מ-URL", "בניית img דינמי מתוך כתובת."),
            ex("E06", "06-html-validation", "HTML Validation", "required, type נכון, טווחים ואורכים."),
            ex("E07", "07-javascript-validation", "JavaScript Validation", "בדיקת includes, alert ו-return."),
            ex("E08", "08-javascript-validation-2", "Validation נוסף", "בדיקת אות ראשונה וסדר בדיקות."),
            ex("E09", "09-deletions", "מחיקה מה-DOM - שלב ביניים", "event.target ו-remove; לא הפתרון הסופי עם Storage."),
            ex("E10", "10-local-storage", "יסודות Local Storage", "setItem/getItem ו-JSON."),
            ex("E11", "11-קובץ הכנה למבחן", "התבנית המרכזית", "SSOT, add, validation, sync ו-delete."),
            ex("E12", "12-homework-dynamic-html-1", "תרגול Dynamic HTML", "יישום נוסף של Form -> Array -> Table."),
        ],
        "homework": [hw("HW01", "Dynamic HTML.docx", "חמש משימות: מצרכים, ציונים, צבעים, תמונות וחיות עם Storage כאתגר.")],
        "rules": [
            rule("TR01", "MUST", "לשים onsubmit על form ובתחילת הפונקציה event.preventDefault().", "01-transcript-with-timestamps.txt", "38:17-43:29", "E03-E12"),
            rule("TR02", "MUST", "Validation בסיסי שניתן לבצע ב-HTML יבוצע ב-HTML וב-type מתאים.", "01-transcript-with-timestamps.txt", "01:39:40-01:50:27", "E06"),
            rule("TR03", "MUST", "ב-JavaScript Validation, alert אינו עוצר; יש לבצע return.", "01-transcript-with-timestamps.txt", "02:10:27-02:13:15", "E07-E08"),
            rule("TR04", "MUST NOT", "במבחן לבנות Dynamic HTML ב-innerHTML; לא createElement ולא append.", "01-transcript-with-timestamps.txt", "33:30-36:11; 01:33:18-01:34:49", "E03-E12"),
            rule("TR05", "MUST", "Local Storage הוא Single Source of Truth; ה-DOM הוא תצוגה בלבד.", "01/02 transcripts", "02:53:20-02:59:55; 28:19-36:11", "E10-E11"),
            rule("TR06", "MUST NOT", "לא לעדכן את ה-DOM בתוך לולאה; לבנות מחרוזת ולעדכן innerHTML פעם אחת אחרי הלולאה.", "01/02 transcripts", "03:47:36-03:51:14; 35:17-36:24", "E11"),
            rule("TR07", "MUST", "מחיקה: confirm -> get array -> splice(index,1) -> save -> sync.", "02-transcript-with-timestamps.txt", "10:28-32:17", "E11"),
            rule("TR08", "ALLOWED", "מותר AI ל-CSS, אך הקוד המוגש חייב להיות קריא, מעוצב ומובן לתלמיד.", "02-transcript-with-timestamps.txt", "33:55-35:13", "All"),
        ],
    },
    {
        "id": "L-2026-08-16",
        "folder": "2026-08-16-preps-for-project1-functions",
        "title": "הכנה לפרויקט, Callbacks, Arrow Functions ו-HOF",
        "source_status": "קיימים קוד כיתה מלא, VTT עם timestamps, תמלול מאוחד ושני שיעורי בית.",
        "learned": [
            "המשך תבנית הפרויקט: תפריט, required דינמי, update, filters ותאריך מרבי.",
            "פונקציה יכולה להישלח כערך וכ-argument לפונקציה אחרת.",
            "callback הוא פונקציה שמועברת ומופעלת מאוחר יותר.",
            "Anonymous Function ו-Arrow Function.",
            "Higher-Order Functions על מערכים: forEach, find, filter, map, reduce.",
        ],
        "syntax": ["callback", "function expression", "=>", "forEach", "find", "findIndex", "filter", "map", "reduce", "includes", "Date", "max"],
        "exercises": [
            ex("E01", "01-dhtml-menu", "תפריט DHTML משותף", "פונקציה שמכניסה קישורים ל-nav בכל דף."),
            ex("E02", "02-dynamic-required-js", "Validation דינמי ב-JS", "תנאי מיוחד באמצעות JavaScript."),
            ex("E03", "03-dynamic-required-html", "שינוי required דינמי", "onchange משנה את required של שדה אחר."),
            ex("E04", "04-updating-a-row", "החזרת נתונים לטופס", "Update מאתר רשומה וממלא את השדות."),
            ex("E05", "05-filtering-page", "דף פילטרים", "בחירה והצגת subset של המידע."),
            ex("E06", "06-max-min-date-validation", "תאריך מינימום/מקסימום", "בניית YYYY-MM-DD והצבה ב-min/max."),
            ex("E07", "07-functions-as-arguments", "פונקציות כ-arguments", "העברת פונקציה בלי להפעיל אותה."),
            ex("E08", "08-invoking-a-callback-function", "הפעלת callback", "הפונקציה המקבלת קוראת callback()."),
            ex("E09A", "09-why-we-need-callbacks", "למה צריך callback", "הפרדת פעולה כללית מהפעולה המשתנה."),
            ex("E09B", "09-why-we-need-callbacks-2", "Callbacks - המשך", "שימוש חוזר באותה פונקציה עם התנהגות שונה."),
            ex("E10", "10-class-exercise-mapping-an-array", "תרגיל map", "המרת כל איבר במערך לתוצאה חדשה."),
            ex("E11", "11-anonymous-functions", "פונקציה אנונימית", "פונקציה ללא שם במקום שבו היא נשלחת."),
            ex("E12", "12-arrow-functions", "Arrow Function", "החלפת function בסימן =>."),
            ex("E13", "13-arrow-functions-strength", "חוזקות Arrow", "כתיבה קצרה של callbacks."),
            ex("E14", "14-arrow-functions-shortened", "Arrow מקוצר", "פרמטר אחד בלי (), שורה אחת בלי {} ו-return."),
            ex("E15", "15-HOF-functions", "Higher-Order Functions", "forEach/find/filter/map/reduce על מערכים."),
        ],
        "homework": [
            hw("HW01", "01 - Callback Functions.docx", "תרגילי callback בארבע צורות: normal, inline, anonymous ו-arrow."),
            hw("HW02", "01 - Higher-Order Functions.docx", "מספרים, נקודות ופיצות באמצעות HOF ולא לולאות ידניות לחישובים."),
        ],
        "rules": [
            rule("TR01", "MUST", "בפרויקט שדות החובה הם קטגוריה, סכום ותאריך; תיאור חובה רק כאשר נבחר Other.", "part-1.vtt", "00:35:27-00:35:42", "Project form"),
            rule("TR02", "MUST", "הפילטרים מוצגים בדף נפרד ולא על אותו דף של טבלת הבית.", "part-1.vtt", "01:03:55-01:04:02", "E05"),
            rule("TR03", "MUST NOT", "לגרפים בפרויקט להשתמש ב-Chart.js ולא בספרייה האחרת שהוצגה.", "part-1.vtt", "01:10:05-01:10:13", "Project reports"),
            rule("TR04", "MUST UNDERSTAND", "reduce היא אחת הפונקציות החשובות ב-JavaScript ובראיונות.", "part-2.vtt", "00:02:11-00:02:21", "E15"),
            rule("TR05", "PREFERRED", "אם כבר עוברים על מערך לצורך side effect, המרצה מעדיף forEach על for...of; לולאות for אינן אסורות בכל מצב.", "part-2.vtt", "00:16:36-00:18:38", "E15"),
            rule("TR06", "PREFERRED", "Arrow עם parameter אחד נכתבת בלי סוגריים; expression יחיד בלי מסולסלים ובלי return מפורש.", "part-1.vtt", "03:28:08-03:34:33", "E12-E14"),
            rule("TR07", "MUST UNDERSTAND", "Function name ללא () הוא הפונקציה; הוספת () היא invocation.", "part-1.vtt", "Callback section", "E07-E08"),
        ],
    },
    {
        "id": "L-2026-08-19",
        "folder": "2026-08-19-async",
        "title": "Asynchronous JavaScript, Promise ו-async/await",
        "source_status": "קיימים 17 תרגילי כיתה, תמלול מלא עם timestamps ושיעורי בית HOF/Callback.",
        "learned": [
            "JavaScript מריץ קוד סינכרוני ב-call stack יחיד.",
            "setTimeout/setInterval ו-event loop מאפשרים עבודה אסינכרונית.",
            "callback יכול להחזיר תוצאה מאוחר יותר אך יוצר קינון.",
            "Promise מייצג פעולה עתידית: pending, fulfilled או rejected.",
            "then/catch מטפלים בהצלחה ובכישלון.",
            "async/await נותנים כתיבה לינארית מעל Promise.",
            "Promise.all מריץ פעולות בלתי תלויות במקביל.",
            "fetch קורא מידע משרת ומחזיר Promise.",
        ],
        "syntax": ["setTimeout", "setInterval", "callback", "new Promise", "resolve", "reject", ".then", ".catch", "async", "await", "try/catch", "Promise.all", "fetch", "response.json"],
        "exercises": [
            ex("E01", "01-homewortk-hof-12", "פתרון HOF", "חזרה על תרגיל 12 משיעורי הבית."),
            ex("E02", "02-javascript-runs-on-a-single-thread", "Single Thread", "סדר הרצת JavaScript."),
            ex("E03", "03-async-example", "דוגמה אסינכרונית", "setTimeout משנה את סדר הפלט."),
            ex("E04", "04-clock", "שעון", "setInterval ועדכון DOM כל שנייה."),
            ex("E05", "05-async-party", "פעולות אסינכרוניות", "כמה פעולות בזמנים שונים."),
            ex("E06", "06-what-happens-when-callstack-no-empty", "Call Stack עמוס", "Callback ממתין עד שה-stack פנוי."),
            ex("E07", "07-event-loop-challenge", "אתגר Event Loop", "חיזוי סדר פלט."),
            ex("E08", "08-get-location", "Geolocation עם callback", "success/error callbacks."),
            ex("E09", "09-hanukkah", "חנוכה עם callbacks", "שרשרת פעולות אסינכרוניות."),
            ex("E10", "10-get-location-promise", "Geolocation עם Promise", "עטיפת callback ב-Promise."),
            ex("E11", "11-hanukkah-promise", "חנוכה עם Promise", "then/catch במקום קינון callbacks."),
            ex("E12", "12-hanukkah-concurrent-promises", "Promises במקביל", "Promise.all לפעולות בלתי תלויות."),
            ex("E13", "13-async-await", "async/await", "המתנה ל-Promise ו-try/catch."),
            ex("E14", "14-hanukkah-async-await", "חנוכה עם async/await", "אותה לוגיקה בכתיבה לינארית."),
            ex("E15", "15-hanukkah-concurrent-async-await", "async/await במקביל", "await על Promise.all."),
            ex("E16", "16-async-function-always-returns-a-promise", "async מחזירה Promise", "גם return רגיל נעטף ב-Promise."),
            ex("E17", "17-get-data-from-server", "fetch", "קריאת שרת ו-response.json()."),
        ],
        "homework": [
            hw("HW01", "01 - Callback Functions.docx", "תרגילי callback בסגנונות function שונים."),
            hw("HW02", "01 - Higher-Order Functions.docx", "תרגילי מערכים עם find/filter/map/reduce."),
        ],
        "rules": [
            rule("TR01", "MUST NOT", "לא להשתמש ב-forEach כדי ליישם בעצמנו filter, map או reduce; לבחור את ה-HOF שמתאימה לתוצאה.", "main.vtt", "00:22:03-00:22:37", "E01"),
            rule("TR02", "MUST UNDERSTAND", "ב-Arrow expression יחיד הערך מוחזר אוטומטית; אין צורך לכתוב return.", "main.vtt", "00:15:07-00:15:43", "HOF callbacks"),
            rule("TR03", "MUST UNDERSTAND", "await אינו חוסם את כל ה-call stack; הוא משהה את הפונקציה האסינכרונית בלבד.", "main.vtt", "03:38:50-03:39:04", "E13-E15"),
            rule("TR04", "PREFERRED", "ב-async/await משתמשים ב-try/catch במקום then/catch סביב אותה פעולה.", "main.vtt", "03:31:33-03:42:09", "E13-E15"),
            rule("TR05", "MUST UNDERSTAND", "פעולות בלתי תלויות שרוצים להריץ במקביל יש לאסוף ב-Promise.all ולא לבצע await סדרתי לכל אחת.", "main.vtt", "03:45:21 ואילך", "E12/E15"),
            rule("TR06", "MUST UNDERSTAND", "async function תמיד מחזירה Promise.", "main.vtt + E16", "03:30:42 ואילך", "E16"),
            rule("TR07", "MUST", "לשלוט ב-reduce; המרצה הדגיש שזה חשוב גם לתרגילים החדשים.", "main.vtt", "03:09:36-03:09:43", "E01"),
        ],
    },
    {
        "id": "L-2026-08-23",
        "folder": "2026-08-23-ajax",
        "title": "Destructuring, Cloning, IIFE, Fetch ו-Aggregation",
        "source_status": "קיימים 13 תרגילי כיתה, תמלול מלא עם timestamps ושלושה שיעורי בית אסינכרוניים.",
        "learned": [
            "Object/Array Destructuring מוציא רק את הנתונים הדרושים.",
            "Spread Operator משכפל אובייקט או מערך.",
            "אין לשנות object/array שהתקבל כ-argument; משכפלים קודם.",
            "IIFE היא פונקציה שמוגדרת ומופעלת מיד.",
            "getData מרכז fetch ו-response.json.",
            "join('') מחבר מערך מחרוזות ל-HTML.",
            "reduce מבצע aggregation: סכום, ממוצע, ספירה וקיבוץ.",
        ],
        "syntax": ["const { a, b } = object", "const [a, b] = array", "...spread", "(async () => { })()", "fetch", "join('')", "reduce", "find", "map", "try/catch"],
        "exercises": [
            ex("E01", "01-object-deconstruction", "Object Destructuring", "פירוק אובייקט מקונן לשדות נבחרים."),
            ex("E02", "02-object-deconstruction-array", "Destructuring בתוך map", "קבלת users מה-JSON ופירוק כל user בפרמטר."),
            ex("E03", "03-array-deconstruction", "Array Destructuring", "קבלת שני האיברים הראשונים מהמערך."),
            ex("E04", "04-cloning", "Cloning ו-Spread", "הבדל primitive/object ושכפול לפני שינוי."),
            ex("E05", "05-iife", "IIFE", "async function שמופעלת מיד."),
            ex("E06", "06-getData", "פונקציית getData", "גרסת async/await וגרסת Promise מקוצרת."),
            ex("E07", "07-class-exercise-1", "Users Table", "fetch users -> destructuring -> map -> reduce -> innerHTML."),
            ex("E08", "08-join", "join", "החלפת reduce שמחבר מחרוזות ב-join('')."),
            ex("E09", "09-class-exercise-2-aggregation", "ממוצע משקל", "reduce לסכום וחלוקה ב-length."),
            ex("E10", "10-class-exercise-3-aggregation", "ממוצע לפי מגדר", "filter ואז reduce לכל קבוצה."),
            ex("E11", "11-class-exercise-4-aggregation", "Aggregation במעבר אחד", "reduce לאובייקט עם sum/count לכל מגדר."),
            ex("E12", "12-class-exercise-5-multi-aggregation", "קיבוץ לפי State", "reduce למערך קבוצות, find, count, map ו-join."),
            ex("E13", "13-class-exercise-6-todos", "ספירת Todos למשתמש", "אותו Pattern של grouping לפי userId."),
        ],
        "homework": [
            hw("HW01", "01 - Asynchronous Functions.docx", "setTimeout/setInterval, callbacks, Geolocation ושעון."),
            hw("HW02", "02 - Promise.docx", "בניית פונקציות שמחזירות Promise ושימוש ב-then/catch."),
            hw("HW03", "03 - async-await.docx", "פתרון פעולות Promise באמצעות async/await ו-try/catch."),
        ],
        "rules": [
            rule("TR01", "MUST UNDERSTAND", "Object Destructuring הוא Syntax חשוב; להוציא רק את השדות שהקוד צריך.", "part-2-main.vtt", "01:07:49-01:08:49", "E01-E03/E07"),
            rule("TR02", "MUST NOT", "לא לשנות אובייקט או מערך שהתקבל כ-argument. יש לשכפל באמצעות spread ורק אז לשנות.", "part-2-main.vtt", "01:24:39-01:29:11; 03:19:34-03:19:42", "E04/E11-E13"),
            rule("TR03", "MUST UNDERSTAND", "חובה להכיר IIFE ולזכור את () האחרונים שמפעילים אותה.", "part-2-main.vtt", "01:45:19-01:45:53", "E05-E13"),
            rule("TR04", "MUST", "כאשר IIFE מופיעה מיד אחרי קוד אחר, לסיים את הפקודה הקודמת בנקודה-פסיק כדי למנוע פירוש שגוי.", "part-2-main.vtt", "02:19:15-02:19:51", "E06-E13"),
            rule("TR05", "PREFERRED", "ליצירת HTML ממערך: map ואז join(''); אין צורך ב-reduce רק כדי לחבר מחרוזות.", "part-2-main.vtt", "02:26:49-02:32:17", "E07-E08"),
            rule("TR06", "MUST UNDERSTAND", "reduce היא לולאה שמרכזת מערך לתוצאה אחת והיא מהפונקציות החשובות ביותר ב-JavaScript.", "part-2-main.vtt", "03:05:01-03:06:47", "E09-E13"),
            rule("TR07", "PREFERRED", "המרצה מעדיף את הסגנון המקוצר של getData שמחזיר את Promise של fetch/response.json.", "part-2-main.vtt", "02:06:31-02:20:11", "E06"),
        ],
    },
    {
        "id": "L-2026-08-26",
        "folder": "2026-08-26-git-github",
        "title": "Git, GitHub, Branches ו-Pull Requests",
        "source_status": "נמצא מסמך כיתה ב-Google Drive ושיעורי בית מקוריים. עדיין אין תמלול הקלטה עם timestamps ולא נוספה תיקיית קוד חדשה ב-Git של המרצה.",
        "learned": [
            "Git מנהל גרסאות והיסטוריה של קוד בתוך Repository.",
            "הטרמינל פועל תמיד מתוך תיקייה מסוימת ולכן חשוב לבדוק את המיקום לפני פקודות קבצים ו-Git.",
            "Staging באמצעות git add מכין שינויים ל-Commit.",
            "Commit שומר נקודת גרסה עם הודעה משמעותית.",
            "GitHub מארח Repository מרוחק ומאפשר שיתוף וסנכרון.",
            "Branch מאפשר לעבוד על משימה בנפרד; Merge מחבר אותה לענף אחר.",
            "Pull Request הוא מנגנון בדיקה ומיזוג של GitHub ודומיו, ולא תכונה בסיסית של Git.",
        ],
        "syntax": [
            "pwd", "ls", "ls -ltra", "cd", "../", "./", "Ctrl+C",
            "git init", "git add filename", "git add .", "git commit -m \"message\"",
            "git config --global user.name", "git config --global user.email",
            "git revert commit-id", "git clone repository-url", "git branch branch-name",
            "git checkout branch-name", "git checkout -b branch-name", "git merge branch-name",
            "git push",
        ],
        "exercises": [
            ex("E01", ".", "מסמך הכיתה Git ו-GitHub", "היכרות עם Repository, Staging, Commit, Clone, Branch, Merge ו-Pull Request."),
        ],
        "homework": [
            hw("HW01", "Git & GitHub.docx", "אתחול פרויקט קודם כ-Repository, ביצוע add/commit, העלאה ל-GitHub ופרסום ב-GitHub Pages."),
            hw("HW02", "Git & GitHub.docx", "בניית אתר פרחים במספר גרסאות, Clone, עבודה ב-Branch, הוספת contact.html, Merge ו-Push אחרון."),
        ],
        "rules": [
            rule("TR01", "MUST UNDERSTAND", "הטרמינל תמיד נמצא בתיקייה מסוימת והפקודות מתבצעות ביחס לתיקייה הזאת.", "Google Docs: git and github", "אין timestamp — מסמך כתוב", "E01/HW01-HW02"),
            rule("TR02", "MUST NOT", "לא להעתיק תיקייה שמכילה .git לתוך תיקייה אחרת שגם מכילה .git.", "Google Docs: git and github", "אין timestamp — מסמך כתוב", "E01"),
            rule("TR03", "PREFERRED", "לכל משימה פותחים Branch נפרד, מבצעים בו Commits, ולאחר בדיקה ממזגים אותו לענף היעד.", "Google Docs: git and github", "אין timestamp — מסמך כתוב", "E01/HW02"),
            rule("TR04", "MUST UNDERSTAND", "Pull Request הוא פיצ'ר של GitHub, GitLab ו-Bitbucket ולא פקודת Git בסיסית.", "Google Docs: git and github", "אין timestamp — מסמך כתוב", "E01"),
            rule("TR05", "MUST", "בשיעורי הבית יש לפרסם את האתר ב-GitHub Pages ולבדוק שהוא ניתן לגלישה גם מהטלפון.", "Git & GitHub.docx", "אין timestamp — מסמך כתוב", "HW01-HW02"),
        ],
    },
]


def lesson_markdown(lesson):
    lines = [
        f"# {lesson['id']} - {lesson['title']}",
        "",
        f"**תיקיית מקור:** `{lesson['folder']}`",
        "",
        f"**מצב המקורות:** {lesson['source_status']}",
        "",
        "## מה למדנו",
        "",
    ]
    lines.extend(f"- {item}" for item in lesson["learned"])

    lines.extend(["", "## פקודות ו-Syntax מרכזיים", ""])
    if lesson["syntax"]:
        lines.extend(f"- `{item}`" for item in lesson["syntax"])
    else:
        lines.append("- אין Syntax מאומת במקורות המקומיים.")

    lines.extend(["", "## תרגילי הכיתה", ""])
    if lesson["exercises"]:
        for item in lesson["exercises"]:
            full_id = f"{lesson['id']}-{item['code']}"
            lines.extend([
                f"### {full_id} - {item['title']}",
                "",
                f"- **תיקייה:** `{item['folder']}`",
                f"- **מה התרגיל מלמד:** {item['purpose']}",
            ])
            if item["syntax"]:
                lines.append(f"- **Syntax מרכזי:** `{item['syntax']}`")
            lines.append("")
    else:
        lines.extend(["אין תיקיות תרגיל מקומיות בשיעור זה.", ""])

    lines.extend(["## שיעורי בית", ""])
    if lesson["homework"]:
        for item in lesson["homework"]:
            full_id = f"{lesson['id']}-{item['code']}"
            lines.extend([
                f"### {full_id}",
                "",
                f"- **קובץ:** `{item['filename']}`",
                f"- **מטרת המשימה:** {item['summary']}",
                "",
            ])
    else:
        lines.extend(["לא נמצא קובץ שיעורי בית.", ""])

    lines.extend(["## Teacher Rules - הוראות ודגשים", ""])
    if lesson["rules"]:
        for item in lesson["rules"]:
            full_id = f"{lesson['id']}-{item['code']}"
            lines.extend([
                f"### {full_id}",
                "",
                f"- **PRIORITY:** `{item['priority']}`",
                f"- **TEACHER RULE:** {item['text']}",
                f"- **SOURCE:** `{item['source']}`",
                f"- **TIMESTAMP:** `{item['timestamp']}`",
            ])
            if item["related"]:
                lines.append(f"- **RELATED:** `{item['related']}`")
            lines.append("")
    else:
        lines.extend([
            "לא סווגה הוראת מרצה מפורשת ממקור ברור. אין להסיק מכך שלא ניתנו הוראות; רק שאין תמלול מספיק לסיווג בטוח.",
            "",
        ])

    lines.extend([
        "## איך לשאול אותי על השיעור",
        "",
        f"אפשר לשלוח: `תסביר לי את {lesson['id']}` או מזהה מדויק של תרגיל/כלל, למשל `{lesson['id']}-E01` או `{lesson['id']}-TR01`.",
        "",
        "## מקורות",
        "",
        f"- תיקיית השיעור המקורית: `{COURSE_ROOT / lesson['folder']}`",
        f"- עותקי התמלול ל-Git: `transcripts/{lesson['id']}/`",
        "",
    ])
    return "\n".join(lines)


def copy_transcripts(lesson):
    source = COURSE_ROOT / lesson["folder"]
    destination = TRANSCRIPTS / lesson["id"]
    destination.mkdir(parents=True, exist_ok=True)

    candidates = []
    transcript_dir = source / "תמלול"
    if transcript_dir.exists():
        candidates.extend(
            p for p in transcript_dir.rglob("*")
            if p.is_file() and p.suffix.lower() in {".txt", ".vtt", ".srt"}
        )

    for p in source.iterdir() if source.exists() else []:
        if p.is_file() and p.suffix.lower() in {".txt", ".vtt"} and "transcript" in p.name.lower():
            candidates.append(p)

    seen = set()
    if candidates:
        no_transcript = destination / "NO-TRANSCRIPT.md"
        if no_transcript.exists():
            no_transcript.unlink()
    for item in candidates:
        key = item.name.lower()
        if key in seen:
            continue
        seen.add(key)
        shutil.copy2(item, destination / item.name)

    if not candidates:
        (destination / "NO-TRANSCRIPT.md").write_text(
            "# No transcript available\n\nלא נמצא תמלול מקומי מאומת לשיעור זה.\n",
            encoding="utf-8",
        )


LESSON_GUIDES.mkdir(parents=True, exist_ok=True)
TRANSCRIPTS.mkdir(parents=True, exist_ok=True)

for lesson in lessons:
    (LESSON_GUIDES / f"{lesson['id']}.md").write_text(lesson_markdown(lesson), encoding="utf-8")
    copy_transcripts(lesson)


id_system = """# מערכת המזהים

המזהים קבועים ונועדו לאפשר שאלה מדויקת בצ'אט.

- `L-YYYY-MM-DD` - שיעור.
- `L-YYYY-MM-DD-E01` - תרגיל כיתה.
- `L-YYYY-MM-DD-HW01` - שיעורי בית.
- `L-YYYY-MM-DD-TR01` - הוראת מרצה מהתמלול.

## רמות Teacher Rule

- `MUST` - חייבים לבצע.
- `MUST NOT` - אסור לבצע בדרך הזאת.
- `PREFERRED` - זו הדרך שהמרצה מעדיף.
- `ALLOWED` - מותר, אבל לא חובה.
- `MUST UNDERSTAND` - חובה להבין את המשמעות, גם אם אין פקודה יחידה שחייבים לכתוב.
- `NEEDS AUDIO` - התמלול אינו ברור; צריך לבדוק וידאו/אודיו בזמן המצוין.

## דוגמאות לשאלות

- `תסביר לי את L-2026-08-23-E04`
- `מה המרצה אמר ב-L-2026-08-16-TR03?`
- `תן לי תרגול על L-2026-08-19-E13`
- `איזה שיעורי בית קשורים ל-reduce?`
"""
(GUIDES / "ID-SYSTEM.md").write_text(id_system, encoding="utf-8")


index = [
    "# אינדקס מדריכי הקורס",
    "",
    "המדריכים מסודרים כרונולוגית. לכל שיעור, תרגיל, שיעורי בית וכלל מרצה יש מזהה קבוע.",
    "",
    "ראו גם: [מערכת המזהים](ID-SYSTEM.md)",
    "",
    "## שיעורים",
    "",
]
for lesson in lessons:
    index.append(f"- [{lesson['id']} - {lesson['title']}](lessons/{lesson['id']}.md)")

index.extend([
    "",
    "## אינדקסים נוספים",
    "",
    "- [כל הוראות המרצה](TEACHER-RULES-INDEX.md)",
    "- [כל שיעורי הבית](HOMEWORK-INDEX.md)",
    "",
    "## סדר לימוד מומלץ",
    "",
    "1. HTML ו-CSS בסיסי.",
    "2. משתנים, תנאים ולולאות.",
    "3. מערכים ואובייקטים.",
    "4. פונקציות ו-return.",
    "5. Strings, JSON ו-DOM.",
    "6. Forms, Validation, Dynamic HTML ו-Local Storage.",
    "7. Callbacks ו-Higher-Order Functions.",
    "8. Asynchronous JavaScript, Promise ו-async/await.",
    "9. Destructuring, Cloning, IIFE, fetch ו-Aggregation.",
    "",
    "## כלל עבודה",
    "",
    "כאשר קיימת הוראה מפורשת של המרצה, היא גוברת על פתרון JavaScript כללי או על Refactor מודרני שלא נלמד בכיתה.",
    "",
])
(GUIDES / "COURSE-INDEX.md").write_text("\n".join(index), encoding="utf-8")


rules_index = [
    "# אינדקס כל הוראות המרצה",
    "",
    "כל כלל מופיע עם מזהה קבוע, רמת חשיבות, מקור ו-timestamp. אם המקור אינו ברור, אין מנחשים.",
    "",
]
for lesson in lessons:
    if not lesson["rules"]:
        continue
    rules_index.extend([
        f"## [{lesson['id']} - {lesson['title']}](lessons/{lesson['id']}.md)",
        "",
    ])
    for item in lesson["rules"]:
        full_id = f"{lesson['id']}-{item['code']}"
        rules_index.extend([
            f"### {full_id}",
            "",
            f"- **PRIORITY:** `{item['priority']}`",
            f"- **TEACHER RULE:** {item['text']}",
            f"- **SOURCE:** `{item['source']}`",
            f"- **TIMESTAMP:** `{item['timestamp']}`",
        ])
        if item["related"]:
            rules_index.append(f"- **RELATED:** `{item['related']}`")
        rules_index.append("")
(GUIDES / "TEACHER-RULES-INDEX.md").write_text("\n".join(rules_index), encoding="utf-8")


homework_index = [
    "# אינדקס כל שיעורי הבית",
    "",
    "כל משימה מקבלת מזהה קבוע. אפשר לשלוח בצ'אט רק את המזהה ולבקש פירוק, הסבר או פתרון לפי סגנון המרצה.",
    "",
]
for lesson in lessons:
    if not lesson["homework"]:
        continue
    homework_index.extend([
        f"## [{lesson['id']} - {lesson['title']}](lessons/{lesson['id']}.md)",
        "",
    ])
    for item in lesson["homework"]:
        full_id = f"{lesson['id']}-{item['code']}"
        homework_index.extend([
            f"### {full_id}",
            "",
            f"- **קובץ:** `{item['filename']}`",
            f"- **מטרת המשימה:** {item['summary']}",
            "",
        ])
(GUIDES / "HOMEWORK-INDEX.md").write_text("\n".join(homework_index), encoding="utf-8")


readme = """# Course Study Guides - JB 45800-9

מאגר לימוד אישי של אברהם יצחק דייטש.

## כניסה מהירה

- [אינדקס כל השיעורים](guides/COURSE-INDEX.md)
- [מערכת המזהים](guides/ID-SYSTEM.md)
- [כל הוראות המרצה](guides/TEACHER-RULES-INDEX.md)
- [כל שיעורי הבית](guides/HOMEWORK-INDEX.md)
- [העלאה בטוחה ל-GitHub](PUBLISH-TO-GITHUB.md)
- `transcripts/` - עותקי התמלולים לפי מזהה שיעור

## עדכון לאחר שיעור חדש

1. מעדכנים את Git של המרצה.
2. יוצרים תיקיית שיעור מקומית עם `תמלול` ו-`שיעורי בית`.
3. מוסיפים מזהים לתרגילים, לשיעורי הבית ול-Teacher Rules.
4. כלל לא ברור מסומן `NEEDS AUDIO` ולא מנחשים אותו.
5. מריצים את `tools/build_guides.py` לאחר עדכון נתוני השיעור.

## הערה

זהו מאגר נפרד ממאגר הקוד של המרצה. אין לדחוף תמלולים או הערות אישיות ל-Git של המרצה ללא הרשאה מפורשת.
"""
(REPO_ROOT / "README.md").write_text(readme, encoding="utf-8")


gitignore = """# Generated/system files
.DS_Store
Thumbs.db
desktop.ini
__pycache__/
*.pyc
"""
(REPO_ROOT / ".gitignore").write_text(gitignore, encoding="utf-8")

print(f"Created {len(lessons)} lesson guides")
