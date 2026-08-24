# העלאה בטוחה ל-GitHub

המאגר הזה נפרד מהמאגר של המרצה. אין להעלות תמלולים או הערות אישיות אל `shaharsol/jb-45800-9` ללא הרשאה מפורשת.

## מה כבר מוכן

- Git מקומי אותחל בענף `main`.
- המדריכים והתמלולים נמצאים ב-commit מקומי.
- לכל תמלול יש תיקייה לפי מזהה השיעור.

## מה צריך כדי לפרסם

צריך ליצור מאגר GitHub בחשבון האישי שלך, למשל בשם `course-study-guides`, ולשלוח לי את הקישור שלו.

לאחר קבלת הקישור אפשר להריץ:

```powershell
git remote add origin https://github.com/USERNAME/course-study-guides.git
git push -u origin main
```

## פרטיות

תמלול עשוי לכלול שמות, שיחות או מידע מהכיתה. לפני יצירת מאגר ציבורי צריך לוודא שמותר לפרסם אותו. אם אין אישור, יש ליצור מאגר `Private` ולשתף רק אנשים מורשים.

## עדכון עתידי

אחרי שיעור חדש:

```powershell
python .\tools\build_guides.py
git add guides transcripts tools
git commit -m "Add lesson YYYY-MM-DD"
git push
```

לפני ה-commit צריך לעדכן ב-`tools/build_guides.py` את סיכום השיעור, התרגילים, שיעורי הבית וכללי המרצה. כלל שאינו ברור מסומן `NEEDS AUDIO` ולא נכתב כניחוש.
