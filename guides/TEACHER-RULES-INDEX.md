# אינדקס כל הוראות המרצה

כל כלל מופיע עם מזהה קבוע, רמת חשיבות, מקור ו-timestamp. אם המקור אינו ברור, אין מנחשים.

## [L-2026-07-29 - פונקציות ו-return](lessons/L-2026-07-29.md)

### L-2026-07-29-TR01

- **PRIORITY:** `PREFERRED`
- **TEACHER RULE:** שם פונקציה צריך לתאר את הפעולה שלה; get מתאים לפונקציה שמחזירה ערך ולא רק מציגה.
- **SOURCE:** `02-transcript-with-timestamps.txt`
- **TIMESTAMP:** `57:57-58:03`
- **RELATED:** `Functions`

### L-2026-07-29-TR02

- **PRIORITY:** `MUST UNDERSTAND`
- **TEACHER RULE:** יש להבדיל בין הפונקציה עצמה לבין invocation: שם בלבד הוא הפונקציה; שם עם () מפעיל אותה.
- **SOURCE:** `02-transcript-with-timestamps.txt`
- **TIMESTAMP:** `43:31-43:50; 02:49:35-02:49:42`
- **RELATED:** `Functions`

### L-2026-07-29-TR03

- **PRIORITY:** `PREFERRED`
- **TEACHER RULE:** פונקציות קטנות מונעות חזרה ומקדמות DRY - Don't Repeat Yourself.
- **SOURCE:** `02-transcript-with-timestamps.txt`
- **TIMESTAMP:** `41:07-41:19`
- **RELATED:** `Functions`

## [L-2026-08-02 - Strings, JSON ופונקציות שימושיות](lessons/L-2026-08-02.md)

### L-2026-08-02-TR01

- **PRIORITY:** `PREFERRED`
- **TEACHER RULE:** כדי לבדוק אם מחרוזת נמצאת במחרוזת אחרת, להשתמש ב-includes; אין צורך לזכור את השיטה ההיסטורית.
- **SOURCE:** `01-transcript-with-timestamps.txt`
- **TIMESTAMP:** `15:01-15:09`
- **RELATED:** `Strings`

### L-2026-08-02-TR02

- **PRIORITY:** `MUST UNDERSTAND`
- **TEACHER RULE:** שמות משתנים המתכנת בוחר; שמות הפונקציות וה-Syntax של JavaScript הם הדברים שצריך לזהות.
- **SOURCE:** `01-transcript-with-timestamps.txt`
- **TIMESTAMP:** `19:27-20:02`
- **RELATED:** `Syntax vocabulary`

### L-2026-08-02-TR03

- **PRIORITY:** `MUST UNDERSTAND`
- **TEACHER RULE:** JSON חשוב כי כמעט כל תקשורת בין אפליקציות משתמשת בו.
- **SOURCE:** `02-transcript-with-timestamps.txt`
- **TIMESTAMP:** `32:43-32:50`
- **RELATED:** `JSON`

### L-2026-08-02-TR04

- **PRIORITY:** `MUST UNDERSTAND`
- **TEACHER RULE:** empty string ו-undefined הם falsy.
- **SOURCE:** `02-transcript-with-timestamps.txt`
- **TIMESTAMP:** `03:58:46 ואילך`
- **RELATED:** `Truthy/Falsy`

## [L-2026-08-05 - DOM, Events ו-Dynamic HTML](lessons/L-2026-08-05.md)

### L-2026-08-05-TR01

- **PRIORITY:** `MUST NOT`
- **TEACHER RULE:** בקורס לא להשתמש ב-querySelector כדרך הראשית; לחפש id מתאים ולעבוד עם getElementById.
- **SOURCE:** `project transcript with timestamps`
- **TIMESTAMP:** `03:00:34-03:00:47`
- **RELATED:** `DOM selection`

### L-2026-08-05-TR02

- **PRIORITY:** `PREFERRED`
- **TEACHER RULE:** שינויי מראה עדיף להגדיר ב-CSS ולהוסיף/להסיר class ב-JavaScript.
- **SOURCE:** `project transcript with timestamps`
- **TIMESTAMP:** `03:27:47-03:28:00`
- **RELATED:** `CSS/DOM`

### L-2026-08-05-TR03

- **PRIORITY:** `MUST`
- **TEACHER RULE:** בתוך form לעבוד עם onsubmit ולא עם onclick של כפתור השליחה.
- **SOURCE:** `part-3 transcript with timestamps`
- **TIMESTAMP:** `15:50-17:08`
- **RELATED:** `Forms`

### L-2026-08-05-TR04

- **PRIORITY:** `PREFERRED`
- **TEACHER RULE:** כאשר רצים על מערך להשתמש ב-for...of ולא ב-for רגילה; for רגילה נשמרת למצב שאין מערך לרוץ עליו.
- **SOURCE:** `project transcript with timestamps`
- **TIMESTAMP:** `03:44:20-03:44:55`
- **RELATED:** `Loops`

### L-2026-08-05-TR05

- **PRIORITY:** `PREFERRED`
- **TEACHER RULE:** Dynamic HTML: הנתונים מגיעים ל-JavaScript והוא מסנכרן אותם ל-DOM באמצעות innerHTML.
- **SOURCE:** `project transcript with timestamps`
- **TIMESTAMP:** `03:46:02-03:46:15`
- **RELATED:** `Dynamic HTML`

## [L-2026-08-09 - טופס, Validation, DHTML, מחיקה ו-Local Storage](lessons/L-2026-08-09.md)

### L-2026-08-09-TR01

- **PRIORITY:** `MUST`
- **TEACHER RULE:** לשים onsubmit על form ובתחילת הפונקציה event.preventDefault().
- **SOURCE:** `01-transcript-with-timestamps.txt`
- **TIMESTAMP:** `38:17-43:29`
- **RELATED:** `E03-E12`

### L-2026-08-09-TR02

- **PRIORITY:** `MUST`
- **TEACHER RULE:** Validation בסיסי שניתן לבצע ב-HTML יבוצע ב-HTML וב-type מתאים.
- **SOURCE:** `01-transcript-with-timestamps.txt`
- **TIMESTAMP:** `01:39:40-01:50:27`
- **RELATED:** `E06`

### L-2026-08-09-TR03

- **PRIORITY:** `MUST`
- **TEACHER RULE:** ב-JavaScript Validation, alert אינו עוצר; יש לבצע return.
- **SOURCE:** `01-transcript-with-timestamps.txt`
- **TIMESTAMP:** `02:10:27-02:13:15`
- **RELATED:** `E07-E08`

### L-2026-08-09-TR04

- **PRIORITY:** `MUST NOT`
- **TEACHER RULE:** במבחן לבנות Dynamic HTML ב-innerHTML; לא createElement ולא append.
- **SOURCE:** `01-transcript-with-timestamps.txt`
- **TIMESTAMP:** `33:30-36:11; 01:33:18-01:34:49`
- **RELATED:** `E03-E12`

### L-2026-08-09-TR05

- **PRIORITY:** `MUST`
- **TEACHER RULE:** Local Storage הוא Single Source of Truth; ה-DOM הוא תצוגה בלבד.
- **SOURCE:** `01/02 transcripts`
- **TIMESTAMP:** `02:53:20-02:59:55; 28:19-36:11`
- **RELATED:** `E10-E11`

### L-2026-08-09-TR06

- **PRIORITY:** `MUST NOT`
- **TEACHER RULE:** לא לעדכן את ה-DOM בתוך לולאה; לבנות מחרוזת ולעדכן innerHTML פעם אחת אחרי הלולאה.
- **SOURCE:** `01/02 transcripts`
- **TIMESTAMP:** `03:47:36-03:51:14; 35:17-36:24`
- **RELATED:** `E11`

### L-2026-08-09-TR07

- **PRIORITY:** `MUST`
- **TEACHER RULE:** מחיקה: confirm -> get array -> splice(index,1) -> save -> sync.
- **SOURCE:** `02-transcript-with-timestamps.txt`
- **TIMESTAMP:** `10:28-32:17`
- **RELATED:** `E11`

### L-2026-08-09-TR08

- **PRIORITY:** `ALLOWED`
- **TEACHER RULE:** מותר AI ל-CSS, אך הקוד המוגש חייב להיות קריא, מעוצב ומובן לתלמיד.
- **SOURCE:** `02-transcript-with-timestamps.txt`
- **TIMESTAMP:** `33:55-35:13`
- **RELATED:** `All`

## [L-2026-08-16 - הכנה לפרויקט, Callbacks, Arrow Functions ו-HOF](lessons/L-2026-08-16.md)

### L-2026-08-16-TR01

- **PRIORITY:** `MUST`
- **TEACHER RULE:** בפרויקט שדות החובה הם קטגוריה, סכום ותאריך; תיאור חובה רק כאשר נבחר Other.
- **SOURCE:** `part-1.vtt`
- **TIMESTAMP:** `00:35:27-00:35:42`
- **RELATED:** `Project form`

### L-2026-08-16-TR02

- **PRIORITY:** `MUST`
- **TEACHER RULE:** הפילטרים מוצגים בדף נפרד ולא על אותו דף של טבלת הבית.
- **SOURCE:** `part-1.vtt`
- **TIMESTAMP:** `01:03:55-01:04:02`
- **RELATED:** `E05`

### L-2026-08-16-TR03

- **PRIORITY:** `MUST NOT`
- **TEACHER RULE:** לגרפים בפרויקט להשתמש ב-Chart.js ולא בספרייה האחרת שהוצגה.
- **SOURCE:** `part-1.vtt`
- **TIMESTAMP:** `01:10:05-01:10:13`
- **RELATED:** `Project reports`

### L-2026-08-16-TR04

- **PRIORITY:** `MUST UNDERSTAND`
- **TEACHER RULE:** reduce היא אחת הפונקציות החשובות ב-JavaScript ובראיונות.
- **SOURCE:** `part-2.vtt`
- **TIMESTAMP:** `00:02:11-00:02:21`
- **RELATED:** `E15`

### L-2026-08-16-TR05

- **PRIORITY:** `PREFERRED`
- **TEACHER RULE:** אם כבר עוברים על מערך לצורך side effect, המרצה מעדיף forEach על for...of; לולאות for אינן אסורות בכל מצב.
- **SOURCE:** `part-2.vtt`
- **TIMESTAMP:** `00:16:36-00:18:38`
- **RELATED:** `E15`

### L-2026-08-16-TR06

- **PRIORITY:** `PREFERRED`
- **TEACHER RULE:** Arrow עם parameter אחד נכתבת בלי סוגריים; expression יחיד בלי מסולסלים ובלי return מפורש.
- **SOURCE:** `part-1.vtt`
- **TIMESTAMP:** `03:28:08-03:34:33`
- **RELATED:** `E12-E14`

### L-2026-08-16-TR07

- **PRIORITY:** `MUST UNDERSTAND`
- **TEACHER RULE:** Function name ללא () הוא הפונקציה; הוספת () היא invocation.
- **SOURCE:** `part-1.vtt`
- **TIMESTAMP:** `Callback section`
- **RELATED:** `E07-E08`

## [L-2026-08-19 - Asynchronous JavaScript, Promise ו-async/await](lessons/L-2026-08-19.md)

### L-2026-08-19-TR01

- **PRIORITY:** `MUST NOT`
- **TEACHER RULE:** לא להשתמש ב-forEach כדי ליישם בעצמנו filter, map או reduce; לבחור את ה-HOF שמתאימה לתוצאה.
- **SOURCE:** `main.vtt`
- **TIMESTAMP:** `00:22:03-00:22:37`
- **RELATED:** `E01`

### L-2026-08-19-TR02

- **PRIORITY:** `MUST UNDERSTAND`
- **TEACHER RULE:** ב-Arrow expression יחיד הערך מוחזר אוטומטית; אין צורך לכתוב return.
- **SOURCE:** `main.vtt`
- **TIMESTAMP:** `00:15:07-00:15:43`
- **RELATED:** `HOF callbacks`

### L-2026-08-19-TR03

- **PRIORITY:** `MUST UNDERSTAND`
- **TEACHER RULE:** await אינו חוסם את כל ה-call stack; הוא משהה את הפונקציה האסינכרונית בלבד.
- **SOURCE:** `main.vtt`
- **TIMESTAMP:** `03:38:50-03:39:04`
- **RELATED:** `E13-E15`

### L-2026-08-19-TR04

- **PRIORITY:** `PREFERRED`
- **TEACHER RULE:** ב-async/await משתמשים ב-try/catch במקום then/catch סביב אותה פעולה.
- **SOURCE:** `main.vtt`
- **TIMESTAMP:** `03:31:33-03:42:09`
- **RELATED:** `E13-E15`

### L-2026-08-19-TR05

- **PRIORITY:** `MUST UNDERSTAND`
- **TEACHER RULE:** פעולות בלתי תלויות שרוצים להריץ במקביל יש לאסוף ב-Promise.all ולא לבצע await סדרתי לכל אחת.
- **SOURCE:** `main.vtt`
- **TIMESTAMP:** `03:45:21 ואילך`
- **RELATED:** `E12/E15`

### L-2026-08-19-TR06

- **PRIORITY:** `MUST UNDERSTAND`
- **TEACHER RULE:** async function תמיד מחזירה Promise.
- **SOURCE:** `main.vtt + E16`
- **TIMESTAMP:** `03:30:42 ואילך`
- **RELATED:** `E16`

### L-2026-08-19-TR07

- **PRIORITY:** `MUST`
- **TEACHER RULE:** לשלוט ב-reduce; המרצה הדגיש שזה חשוב גם לתרגילים החדשים.
- **SOURCE:** `main.vtt`
- **TIMESTAMP:** `03:09:36-03:09:43`
- **RELATED:** `E01`

## [L-2026-08-23 - Destructuring, Cloning, IIFE, Fetch ו-Aggregation](lessons/L-2026-08-23.md)

### L-2026-08-23-TR01

- **PRIORITY:** `MUST UNDERSTAND`
- **TEACHER RULE:** Object Destructuring הוא Syntax חשוב; להוציא רק את השדות שהקוד צריך.
- **SOURCE:** `part-2-main.vtt`
- **TIMESTAMP:** `01:07:49-01:08:49`
- **RELATED:** `E01-E03/E07`

### L-2026-08-23-TR02

- **PRIORITY:** `MUST NOT`
- **TEACHER RULE:** לא לשנות אובייקט או מערך שהתקבל כ-argument. יש לשכפל באמצעות spread ורק אז לשנות.
- **SOURCE:** `part-2-main.vtt`
- **TIMESTAMP:** `01:24:39-01:29:11; 03:19:34-03:19:42`
- **RELATED:** `E04/E11-E13`

### L-2026-08-23-TR03

- **PRIORITY:** `MUST UNDERSTAND`
- **TEACHER RULE:** חובה להכיר IIFE ולזכור את () האחרונים שמפעילים אותה.
- **SOURCE:** `part-2-main.vtt`
- **TIMESTAMP:** `01:45:19-01:45:53`
- **RELATED:** `E05-E13`

### L-2026-08-23-TR04

- **PRIORITY:** `MUST`
- **TEACHER RULE:** כאשר IIFE מופיעה מיד אחרי קוד אחר, לסיים את הפקודה הקודמת בנקודה-פסיק כדי למנוע פירוש שגוי.
- **SOURCE:** `part-2-main.vtt`
- **TIMESTAMP:** `02:19:15-02:19:51`
- **RELATED:** `E06-E13`

### L-2026-08-23-TR05

- **PRIORITY:** `PREFERRED`
- **TEACHER RULE:** ליצירת HTML ממערך: map ואז join(''); אין צורך ב-reduce רק כדי לחבר מחרוזות.
- **SOURCE:** `part-2-main.vtt`
- **TIMESTAMP:** `02:26:49-02:32:17`
- **RELATED:** `E07-E08`

### L-2026-08-23-TR06

- **PRIORITY:** `MUST UNDERSTAND`
- **TEACHER RULE:** reduce היא לולאה שמרכזת מערך לתוצאה אחת והיא מהפונקציות החשובות ביותר ב-JavaScript.
- **SOURCE:** `part-2-main.vtt`
- **TIMESTAMP:** `03:05:01-03:06:47`
- **RELATED:** `E09-E13`

### L-2026-08-23-TR07

- **PRIORITY:** `PREFERRED`
- **TEACHER RULE:** המרצה מעדיף את הסגנון המקוצר של getData שמחזיר את Promise של fetch/response.json.
- **SOURCE:** `part-2-main.vtt`
- **TIMESTAMP:** `02:06:31-02:20:11`
- **RELATED:** `E06`
