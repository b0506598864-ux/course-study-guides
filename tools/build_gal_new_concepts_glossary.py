from pathlib import Path
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_teacher_transition_doc import (  # noqa: E402
    BLUE,
    DARK,
    LIGHT_BLUE,
    LIGHT_GOLD,
    LIGHT_GRAY,
    MID_GRAY,
    WHITE,
    add_callout,
    add_heading,
    add_page_number,
    add_table,
    add_text,
    configure_document,
    set_cell_shading,
    set_font,
    set_rtl,
    set_table_geometry,
)


OUTPUT = ROOT / "output" / "docx" / "מילון-המושגים-החדשים-של-גל.docx"


def set_ltr(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_pr = paragraph._p.get_or_add_pPr()
    bidi = p_pr.find(qn("w:bidi"))
    if bidi is None:
        bidi = OxmlElement("w:bidi")
        p_pr.append(bidi)
    bidi.set(qn("w:val"), "0")


def set_code_font(run, size=9.2):
    run.font.name = "Consolas"
    r_pr = run._element.get_or_add_rPr()
    r_pr.rFonts.set(qn("w:ascii"), "Consolas")
    r_pr.rFonts.set(qn("w:hAnsi"), "Consolas")
    r_pr.rFonts.set(qn("w:cs"), "Consolas")
    run.font.size = Pt(size)
    run.font.color.rgb = RGBColor.from_string("17324D")
    rtl = r_pr.find(qn("w:rtl"))
    if rtl is None:
        rtl = OxmlElement("w:rtl")
        r_pr.append(rtl)
    rtl.set(qn("w:val"), "0")


def add_code(doc, code):
    table = doc.add_table(rows=1, cols=1)
    set_table_geometry(table, [9360])
    tbl_pr = table._tbl.tblPr
    bidi = tbl_pr.find(qn("w:bidiVisual"))
    if bidi is not None:
        bidi.set(qn("w:val"), "0")
    cell = table.cell(0, 0)
    set_cell_shading(cell, "F5F7FA")
    p = cell.paragraphs[0]
    set_ltr(p)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    r = p.add_run(code)
    set_code_font(r)
    doc.add_paragraph().paragraph_format.space_after = Pt(1)


def add_label_line(doc, label, text, color=DARK, after=3):
    p = doc.add_paragraph()
    set_rtl(p)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = 1.18
    r = p.add_run(f"{label}: ")
    set_font(r, size=10.3, bold=True, color=color)
    r = p.add_run(text)
    set_font(r, size=10.3)
    return p


def add_concept(doc, num, item):
    p = doc.add_paragraph()
    set_rtl(p)
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(f"{num}. {item['term']}")
    set_font(r, size=12, bold=True, color=BLUE)
    r = p.add_run(f" — {item['he']}")
    set_font(r, size=11.5, bold=True, color=DARK)
    add_label_line(doc, "בפשטות", item["simple"])
    add_label_line(doc, "מתי משתמשים", item["when"])
    add_label_line(doc, "מה קבוע ומה בוחרים", item["fixed"])
    if item.get("code"):
        add_code(doc, item["code"])
    if item.get("warning"):
        add_callout(doc, "שימו לב", item["warning"], LIGHT_GOLD)


def add_category(doc, title, intro, items, start_num, new_page=False):
    if new_page:
        doc.add_page_break()
    add_heading(doc, title, 1)
    add_text(doc, intro, size=10.5, color=MID_GRAY, after=8)
    num = start_num
    for item in items:
        add_concept(doc, num, item)
        num += 1
    return num


def item(term, he, simple, when, fixed, code="", warning=""):
    return {
        "term": term,
        "he": he,
        "simple": simple,
        "when": when,
        "fixed": fixed,
        "code": code,
        "warning": warning,
    }


def build_document():
    doc = Document()
    configure_document(doc)

    section = doc.sections[0]
    hp = section.header.paragraphs[0]
    hp.clear()
    set_rtl(hp)
    r = hp.add_run("המילון של גל | FS AI 45800-9")
    set_font(r, size=9, bold=True, color=MID_GRAY)
    fp = section.footer.paragraphs[0]
    fp.clear()
    add_page_number(fp)

    for _ in range(2):
        doc.add_paragraph()
    p = doc.add_paragraph()
    set_rtl(p, WD_ALIGN_PARAGRAPH.CENTER)
    r = p.add_run("המילון של גל")
    set_font(r, size=29, bold=True, color=DARK)
    p.paragraph_format.space_after = Pt(7)
    p = doc.add_paragraph()
    set_rtl(p, WD_ALIGN_PARAGRAPH.CENTER)
    r = p.add_run("כל המושגים החדשים בעברית פשוטה")
    set_font(r, size=17, bold=True, color=BLUE)
    p.paragraph_format.space_after = Pt(8)
    p = doc.add_paragraph()
    set_rtl(p, WD_ALIGN_PARAGRAPH.CENTER)
    r = p.add_run("שיעורי גל: Git וכלי AI • JavaScript מודרני • TypeScript • Node.js ו־npm")
    set_font(r, size=11.5, color=MID_GRAY)
    p.paragraph_format.space_after = Pt(22)

    add_callout(
        doc,
        "המטרה",
        "לא לשנן אנגלית. להבין מה כל מילה אומרת, מתי משתמשים בה, והאם זו פקודה קבועה או שם שהמתכנת המציא.",
        LIGHT_BLUE,
    )
    add_callout(
        doc,
        "חשוב",
        "המסמך מסביר רק מושגים שהופיעו בקוד, ב־README או בתמלולים של השיעורים החדשים הזמינים עד 2.9.2026. הוא אינו מוסיף חומר מתקדם שלא הופיע.",
        LIGHT_GOLD,
    )

    add_heading(doc, "איך לקרוא כל דוגמת קוד", 1)
    rows = [
        ("מילה קבועה", "חלק מהשפה או מהכלי. כותבים בדיוק, למשל function, type, npm install."),
        ("שם שהמתכנת בוחר", "אפשר לבחור שם אחר, למשל customerName, Employee או compile."),
        ("ערך שהמתכנת בוחר", "המידע עצמו, למשל 20, true או \"Maya\"."),
        ("סימן קבוע", "סימן בעל משמעות בשפה, למשל :, ?, |, &, => או {}."),
    ]
    add_table(doc, ["סוג", "איך מזהים"], rows, [2500, 6860])

    add_heading(doc, "מפת הלימוד", 1)
    add_text(doc, "הסדר המומלץ למתחיל:")
    for line in (
        "1. קודם להבין TypeScript וטיפוסים בסיסיים.",
        "2. אחר כך להבין את מבנה הפרויקט: src, dist, package.json ו־tsconfig.json.",
        "3. לאחר מכן ללמוד את פקודות npm ו־tsc.",
        "4. רק אז לעבור לטיפוסים המתקדמים: union, type alias, optional ו־intersection.",
        "5. בנפרד: Git, כלי AI ו־JavaScript מודרני מהשיעור הקודם.",
    ):
        add_text(doc, line, after=3)

    doc.add_page_break()
    n = 1
    basic_ts = [
        item("TypeScript", "טייפסקריפט", "JavaScript בתוספת מערכת שבודקת אילו סוגי ערכים מותר להכניס לקוד.", "כשאנחנו רוצים לגלות טעויות עוד בזמן הכתיבה, לפני שהתוכנית רצה.", "TypeScript הוא שם השפה. קובץ המקור מסתיים ב־.ts.", "const price: number = 19.9;"),
        item("Type / Typing", "טיפוס / הגדרת טיפוסים", "תיאור של סוג המידע: טקסט, מספר, אמת/שקר או מבנה מורכב.", "כשמגדירים משתנה, פרמטר, תוצאת פונקציה או אובייקט.", "שם הטיפוס המובנה קבוע; שם המשתנה נבחר.", "const customerName: string = \"Maya\";"),
        item("Type safety", "בטיחות טיפוסים", "TypeScript מונעת מאיתנו להשתמש בערך מהסוג הלא נכון.", "כדי לגלות למשל שנשלח טקסט לפונקציה שמחכה למספר.", "זה מושג, לא פקודה שכותבים בקוד.", "calcSubtotal(\"20\", 3); // TypeScript error"),
        item("Static check", "בדיקה לפני הריצה", "העורך או הקומפיילר בודקים את הקוד בלי להפעיל אותו.", "בזמן כתיבת TypeScript ובזמן הפעלת tsc.", "זה מושג. הודעת השגיאה מגיעה מ־TypeScript.", warning="גל הדגיש: זו אינה בדיקת Unit Test ואינה בדיקת Runtime."),
        item("Runtime", "זמן ריצה", "הרגע שבו JavaScript באמת פועלת בדפדפן או ב־Node.", "כשבודקים מה קורה עם מידע אמיתי שהגיע ממשתמש או משרת.", "זה מושג, לא פקודה.", warning="בדיקת TypeScript לא מחליפה Validation בזמן ריצה. גל אמר ששני הדברים אינם באים אחד על חשבון השני."),
        item("string", "מחרוזת / טקסט", "טיפוס של מילים ותווים.", "לשמות, אימייל, מזהה טקסטואלי או משפט קבלה.", "string קבוע; שם המשתנה והטקסט נבחרים.", "const productName: string = \"Notebook\";"),
        item("number", "מספר", "טיפוס אחד לכל המספרים ב־TypeScript: שלמים ועשרוניים.", "למחיר, כמות, גיל, אחוז ומזהה מספרי.", "number קבוע; שם המשתנה והמספר נבחרים.", "const unitPrice: number = 19.9;"),
        item("boolean", "אמת או שקר", "טיפוס שמכיל רק true או false.", "לשאלות כן/לא, למשל האם הלקוח חבר או האם המוצר שולם.", "boolean, true ו־false קבועים; שם המשתנה נבחר.", "const isMember: boolean = true;"),
        item("null", "אין ערך בכוונה", "ערך שמסמן שבכוונה אין כרגע מידע.", "כאשר רוצים לייצג חוסר ערך בצורה מפורשת.", "null היא מילה קבועה.", "let selectedUser: User | null = null;"),
        item("undefined", "עדיין לא הוגדר", "ערך שמופיע כאשר אין ערך או ששדה לא קיים.", "למשל כאשר קוראים שדה אופציונלי שלא הוכנס.", "undefined היא מילה קבועה.", "employee.phone // may be undefined"),
        item("any", "כל סוג", "מכבה כמעט את בדיקת הטיפוסים עבור אותו ערך.", "רק במצב חריג וזמני כאשר עדיין לא יודעים את הטיפוס.", "any קבוע.", "let data: any;", "גל אמר שבדרך כלל לא משתמשים ב־any ושזו דרך לא טובה, כי היא מבטלת את היתרון של TypeScript."),
        item("Type annotation", "כתיבת הטיפוס ליד השם", "הנקודתיים והטיפוס שאחריהם אומרים ל־TypeScript איזה ערך מותר.", "כשגל מבקש טיפוס מפורש למשתנה או לפרמטר.", ": והטיפוס קבועים; variableName הוא שם נבחר.", "const variableName: number = 10;"),
        item("Type inference", "הסקת טיפוס אוטומטית", "TypeScript מבינה את הטיפוס לפי הערך גם אם לא כתבנו אותו.", "כשערך ההתחלה ברור, למשל const price = 20.", "זה מושג. שם המשתנה והערך נבחרים.", "const price = 20; // inferred as number"),
    ]
    n = add_category(doc, "חלק א׳ — יסודות TypeScript", "אלה המושגים החשובים ביותר מהשיעור. כדאי להבין אותם לפני כל השאר.", basic_ts, n)

    function_ts = [
        item("Parameter type", "טיפוס של פרמטר", "קובע איזה סוג ערך מותר להכניס לפונקציה.", "בכל פרמטר של פונקציית TypeScript בתרגיל.", "שם הפרמטר נבחר; : number קבוע לפי הסוג הדרוש.", "function isAdult(age: number): boolean {\n  return age >= 18;\n}"),
        item("Return type", "טיפוס הערך שחוזר", "הטיפוס שכתוב אחרי סוגרי הפרמטרים וקובע מה הפונקציה חייבת להחזיר.", "כאשר מוסיפים טיפוסים לפונקציה.", "הנקודתיים והטיפוס קבועים; גוף הפונקציה נכתב לפי המשימה.", "function calcSubtotal(price: number, quantity: number): number {\n  return price * quantity;\n}"),
        item("void", "לא מחזירה ערך", "טיפוס תוצאה לפונקציה שמבצעת פעולה אבל אינה מחזירה מידע בעזרת return.", "למשל פונקציה שמדפיסה או מעדכנת את הדף.", "void קבוע; שם הפונקציה נבחר.", "function init(): void {\n  console.log(\"start\");\n}"),
        item("Object type", "טיפוס של אובייקט", "תבנית שמפרטת אילו שדות צריכים להיות באובייקט ומה הטיפוס של כל שדה.", "כאשר רוצים לוודא שלכל עובד יש name, id ו־email.", "שמות השדות והטיפוס המותאם נבחרים; התחביר { field: type } קבוע.", "type Employee = {\n  name: string;\n  id: number;\n  email: string;\n};"),
        item("Nested object", "אובייקט בתוך אובייקט", "שדה אחד מכיל אובייקט נוסף עם שדות משלו.", "למשל כתובת בתוך חברה או עובד.", "שמות address, city וכדומה נבחרים; מבנה הסוגריים קבוע.", "address: { street: string; city: string };"),
        item("Array<T>", "מערך של טיפוס מסוים", "אומר שכל האיברים במערך צריכים להתאים לטיפוס שבין < >.", "למשל מערך עובדים או מערך מזהים.", "Array והסוגריים הזוויתיים קבועים; Employee הוא טיפוס שהמתכנת הגדיר.", "const employees: Array<Employee> = [];"),
        item("Generic angle brackets < >", "סוגריים זוויתיים של טיפוס", "ב־Array<Employee> הם אומרים מהו טיפוס האיברים שבתוך המערך.", "כאשר משתמשים בטיפוס כללי כמו Array או ReturnType.", "הסימנים < > קבועים; הטיפוס שבתוכם משתנה לפי הצורך.", "Array<number | string>"),
        item("Optional property ?", "שדה לא חובה", "סימן שאלה אחרי שם שדה אומר שמותר לאובייקט להגיע גם בלי השדה הזה.", "כאשר למשל לא לכל עובד יש phone או address.", "? קבוע; phone הוא שם שדה נבחר.", "phone?: string;"),
        item("Union |", "או", "הערך יכול להתאים לטיפוס אחד או לטיפוס אחר.", "כאשר מזהה יכול להיות number או string, או כאשר status מוגבל לכמה אפשרויות.", "הסימן | קבוע; הטיפוסים והאפשרויות נבחרים.", "function addId(id: number | string): void {}"),
        item("Literal union", "רשימת ערכים מותרים", "לא רק סוג טקסט, אלא טקסטים מסוימים בלבד.", "כאשר status חייב להיות אחת מכמה אפשרויות קבועות.", "| והמירכאות קבועים; המילים active וכו׳ נבחרות לפי הדרישה.", "status: 'active' | 'inactive' | 'closed';"),
        item("Intersection &", "וגם", "הערך חייב לכלול את הדרישות של שני טיפוסים יחד.", "כאשר משתמש צריך להיות גם User וגם Employee.", "& קבוע; שמות הטיפוסים נבחרים.", "type UserType = User & Employee;"),
        item("Type alias", "שם לטיפוס מותאם", "נותנים שם לתיאור של מבנה או שילוב טיפוסים כדי להשתמש בו שוב.", "כאשר מבנה חוזר או מורכב, למשל Employee או Company.", "type קבוע; Employee ושמות השדות נבחרים.", "type Employee = { name: string; id: number };", "בתרגילי Primitive Types גל כתב במפורש לא להוסיף עדיין type alias או interface. הם הופיעו בהדגמה מאוחרת יותר, לא בשלב הראשון של התרגיל."),
        item("Custom type", "טיפוס שהמתכנת יצר", "טיפוס שאינו string/number/boolean אלא תיאור שמתאים לבעיה שלנו.", "למשל טיפוס Employee לפרטי עובד.", "התחביר קבוע; שם הטיפוס וכל השדות נבחרים.", "type Employee = { name: string; email: string };"),
        item("typeof in a type", "יצירת טיפוס מערך קיים", "TypeScript מסתכלת על המבנה של ערך קיים ובונה ממנו טיפוס.", "כאשר כבר יש אובייקט, למשל JSON של מדינה, ורוצים טיפוס באותו מבנה.", "typeof קבוע; country הוא שם משתנה נבחר.", "type Country = typeof country;"),
        item("ReturnType", "טיפוס התוצאה של פונקציה", "כלי מובנה שמחלץ את הטיפוס שפונקציה מחזירה.", "כאשר רוצים להשתמש בטיפוס התוצאה בלי לכתוב אותו שוב ידנית.", "ReturnType ו־typeof קבועים; שם הפונקציה נבחר.", "type CountResult = ReturnType<typeof getEmployeeCount>;"),
        item("Function signature", "חתימת פונקציה", "מתארת אילו פרמטרים פונקציה מקבלת ומה היא מחזירה, בלי לכתוב את הפעולה עצמה.", "כאשר שדה בתוך אובייקט צריך להכיל פונקציה.", "הסוגריים, => והטיפוס קבועים; שם השדה נבחר.", "getEmployeeCount: () => number;"),
        item("Type assertion / as", "אמירה ל־TypeScript: תתייחס לזה כטיפוס", "אנחנו מבטיחים ל־TypeScript שהערך מתאים לטיפוס, גם אם היא לא הצליחה להוכיח זאת.", "רק כאשר אנחנו באמת יודעים את מבנה הערך והיא אינה יודעת.", "as קבוע; Company הוא טיפוס נבחר.", "return {} as Company;", "as אינו יוצר את השדות, אינו בודק מידע בזמן ריצה ועלול להסתיר טעות. גל אמר במפורש שהאובייקט הריק בדוגמה אינו דרך נכונה; הוא השתמש בו רק כדי להדגים casting."),
        item("Casting", "המרת/כפיית התייחסות לטיפוס", "השם המקצועי לפעולה שגל הדגים עם as.", "כאשר צריך לומר למערכת הטיפוסים איך להתייחס לערך.", "זה מושג; בדוגמה התחביר הוא as Company."),
        item("interface", "חוזה למבנה נתונים", "דרך נוספת ב־TypeScript לתאר אילו שדות יש באובייקט.", "בהמשך, כאשר המרצה ילמד ממשקי טיפוסים.", "interface קבוע; שם הממשק והשדות נבחרים.", warning="המושג הוזכר, אבל גל ביקש לא להשתמש בו בתרגילי ה־Primitive Types הראשונים."),
        item("enum", "קבוצת אפשרויות בעלות שמות", "אפשרות TypeScript להגדיר רשימת ערכים קשורה.", "רק אם המרצה ילמד וידרוש זאת בהמשך.", "enum קבוע; שם הרשימה והערכים נבחרים.", warning="enum רק הוזכר כהבדל בין JavaScript ל־TypeScript; הוא לא נדרש בתרגילים שנבדקו."),
    ]
    n = add_category(doc, "חלק ב׳ — טיפוסים בפונקציות ובאובייקטים", "כאן מתחילים לראות יותר סימנים. בכל דוגמה חשוב לזהות מה קבוע ומה גל או המתכנת בחרו.", function_ts, n)

    project_items = [
        item("Compiler / tsc", "הקומפיילר של TypeScript", "תוכנית שקוראת קובצי .ts ובונה מהם קובצי .js.", "אחרי כתיבת TypeScript ולפני שהדפדפן מריץ את הקוד.", "tsc היא פקודה קבועה.", "tsc"),
        item("Compile / Transpile", "תרגום הקוד", "העברת הקוד מ־TypeScript ל־JavaScript. גל אמר שהמונח המדויק יותר הוא transpile, אבל בשיעור הוא משתמש גם במילה compile.", "כאשר רוצים ליצור JavaScript שאפשר להריץ.", "אלה מושגים; הפקודה בפועל היא tsc.", "src/index.ts  ->  tsc  ->  dist/index.js"),
        item("Node.js", "סביבת הרצת JavaScript מחוץ לדפדפן", "תוכנה שמאפשרת להריץ JavaScript במחשב ומגיעה עם npm.", "להפעלת כלי פיתוח כמו TypeScript ולפעמים להרצת JS בטרמינל.", "node הוא שם הכלי והפקודה.", "node -v"),
        item("npm", "מנהל החבילות של Node", "כלי שמתקין ספריות ומריץ פקודות שמוגדרות בפרויקט.", "כאשר מתחילים פרויקט, מתקינים חבילה או מריצים script.", "npm הוא שם קבוע. שמות החבילות וה־script משתנים.", "npm install"),
        item("Package / Library", "חבילה / ספריית קוד", "קוד שמישהו אחר כתב ואפשר להתקין ולהשתמש בו בפרויקט.", "כאשר לא רוצים לבנות כל יכולת מאפס.", "זה מושג; שם החבילה נבחר, למשל axios."),
        item("Dependency", "תלות של הפרויקט", "חבילה שהפרויקט צריך כדי לעבוד.", "כאשר מתקינים ספרייה שהקוד משתמש בה בזמן ריצה.", "dependencies הוא שם שדה קבוע ב־package.json; שמות החבילות נבחרים.", "npm i axios"),
        item("devDependency", "תלות לפיתוח בלבד", "חבילה שנחוצה בזמן הכתיבה או הבנייה, אבל לא להפעלת המוצר הסופי.", "למשל TypeScript שמתרגמת את הקוד לפני העלאה.", "devDependencies קבוע ב־package.json; שם החבילה נבחר.", "npm i typescript --save-dev"),
        item("Production", "סביבת המוצר האמיתי", "הגרסה שהמשתמשים מפעילים, בניגוד לסביבת הפיתוח.", "כאשר מסבירים אילו חבילות צריכות לעלות עם המוצר.", "זה מושג, לא פקודה."),
        item("Development", "סביבת הפיתוח", "השלב שבו אנחנו כותבים, בודקים ומקמפלים את הקוד.", "בזמן העבודה שלנו כמפתחים.", "זה מושג, לא פקודה."),
        item("Global install -g", "התקנה לכל המחשב", "הפקודה זמינה בכל פרויקט במחשב.", "כאשר גל רוצה שהפקודה tsc תעבוד מכל תיקייה.", "-g הוא flag קבוע; שם החבילה נבחר.", "npm i typescript -g"),
        item("Local install", "התקנה בתוך פרויקט אחד", "החבילה נשמרת עבור התיקייה הנוכחית בלבד.", "כאשר רוצים שלכל פרויקט תהיה גרסה משלו.", "זה מושג; npm i typescript --save-dev מבצע התקנה מקומית."),
        item("Flag", "אפשרות נוספת לפקודה", "חלק שמתחיל בדרך כלל במקף ומשנה את אופן הפעולה של הפקודה.", "למשל כדי להתקין גלובלית או כחבילת פיתוח.", "ה־flag קבוע; למשל -g או --save-dev.", "npm i typescript --save-dev"),
        item("Axios", "ספרייה לבקשות HTTP", "ספרייה שעוזרת לשלוח בקשות לשרת, בדומה ל־Ajax GET שלמדתם.", "בהמשך, כאשר צריך להביא מידע מ־API.", "axios הוא שם חבילה קבוע.", "npm i axios", "בשיעור היא הותקנה והוסברה, אך בקוד שנבדק עדיין לא נעשה בה שימוש ממשי."),
        item("HTTP request", "בקשה לשרת", "הודעה שהתוכנית שולחת לשרת כדי לקבל או לשלוח מידע.", "למשל קבלת רשימת מוצרים מ־API.", "זה מושג. GET הוא אחד מסוגי הבקשות."),
        item("Open source", "קוד פתוח", "קוד שאנשים מפרסמים כדי שאחרים יוכלו להשתמש בו ולתרום לו.", "כאשר מתקינים חבילות ציבוריות דרך npm.", "זה מושג, לא פקודה."),
    ]
    n = add_category(doc, "חלק ג׳ — Node.js, npm וחבילות", "המילים האלה אינן פקודות JavaScript רגילות. הן שייכות לסביבת העבודה ולניהול הפרויקט.", project_items, n)

    files_items = [
        item("package.json", "תעודת הזהות של הפרויקט", "קובץ שמכיל שם, גרסה, scripts ורשימת חבילות.", "אחרי npm init ובכל פרויקט Node/npm.", "שם הקובץ והשדות המרכזיים קבועים; שם הפרויקט וה־scripts נבחרים.", '"scripts": { "compile": "tsc --watch" }'),
        item("package-lock.json", "נעילת גרסאות החבילות", "קובץ שנוצר אוטומטית ושומר אילו גרסאות מדויקות הותקנו.", "npm יוצרת ומעדכנת אותו בזמן התקנה.", "שם הקובץ קבוע. בדרך כלל לא עורכים אותו ביד."),
        item("node_modules", "תיקיית החבילות המותקנות", "תיקייה גדולה שמכילה את הקוד של כל החבילות והתלויות שלהן.", "נוצרת אחרי npm install.", "שם התיקייה קבוע. לא עורכים את הקבצים בתוכה.", warning="אם התיקייה חסרה, מריצים npm install. בדרך כלל לא מעלים node_modules ל־Git."),
        item("tsconfig.json", "הגדרות TypeScript", "קובץ שאומר לקומפיילר מאיפה לקרוא, לאן לכתוב ואילו בדיקות להפעיל.", "בפרויקט TypeScript, אחרי tsc --init.", "שם הקובץ ושמות האפשרויות קבועים; הערכים מותאמים לפרויקט."),
        item("src", "Source — קוד המקור", "התיקייה שבה אנחנו כותבים את קובצי TypeScript.", "בזמן פיתוח.", "src הוא שם מקובל שהמרצה בחר במבנה הפרויקט; הוא אינו פקודת שפה."),
        item("dist", "Distribution — הקוד שנוצר", "התיקייה שאליה tsc כותבת JavaScript מוכן להרצה.", "אחרי קומפילציה.", "dist הוא שם מקובל שהוגדר ב־outDir; לא עורכים את ה־JS שנוצר ביד."),
        item("rootDir", "תיקיית המקור לקומפילציה", "אומרת ל־TypeScript איפה נמצאים קובצי .ts.", "בתוך compilerOptions ב־tsconfig.json.", "rootDir קבוע; ./src הוא נתיב שהמתכנת בוחר.", '"rootDir": "./src"'),
        item("outDir", "תיקיית הפלט", "אומרת איפה לשמור את קובצי .js שנוצרו.", "בתוך tsconfig.json.", "outDir קבוע; ./dist הוא נתיב נבחר.", '"outDir": "./dist"'),
        item("strict", "בדיקות טיפוסים מחמירות", "מפעילה קבוצה של בדיקות שעוזרות למצוא יותר טעויות.", "בפרויקט TypeScript שבו רוצים בדיקה חזקה.", "strict קבוע; true מפעיל.", '"strict": true'),
        item("noEmitOnError", "לא ליצור JS כשיש שגיאה", "אם TypeScript מוצאת שגיאה, היא לא מוציאה קובץ JavaScript חדש.", "כדי לא להריץ בטעות פלט שנבנה מקוד שגוי.", "noEmitOnError קבוע; true מפעיל.", '"noEmitOnError": true'),
        item("include", "מה כן לכלול", "רשימה של קבצים או תיקיות שהקומפיילר צריך לבדוק.", "ב־tsconfig.json כאשר רוצים להגביל את הקומפילציה.", "include קבוע; הנתיבים נבחרים.", '"include": ["./**/*.ts"]'),
        item("exclude", "ממה להתעלם", "רשימת תיקיות שלא צריך לקמפל.", "כדי לדלג על node_modules ועל קוד פלט.", "exclude קבוע; שמות התיקיות נבחרים.", '"exclude": ["node_modules", "dist"]'),
        item("target", "גרסת JavaScript לפלט", "קובעת לאיזו רמת JavaScript TypeScript תתרגם.", "כאשר צריך להתאים לסביבה שתפעיל את הקוד.", "target קבוע; ES2020 או esnext הם ערכים נבחרים.", '"target": "ES2020"'),
        item("script in package.json", "קיצור דרך לפקודה", "שם נוח שנותנים לפקודת טרמינל ארוכה.", "כדי להריץ npm run compile במקום לזכור את הפקודה המלאה.", "scripts ו־npm run קבועים; compile הוא שם שהמתכנת בחר.", '"compile": "tsc --watch"'),
        item("Source of truth", "המקור הקובע", "המקום שבו נמצאת הגרסה שעל פיה כולם עובדים.", "בשיעורי גל: ה־Repository וה־README הם המקור לחומר ולהוראות.", "זה מושג, לא פקודה."),
    ]
    n = add_category(doc, "חלק ד׳ — הקבצים והתיקיות בפרויקט", "אם מבינים מי נכתב ביד ומי נוצר אוטומטית, מבנה הפרויקט נעשה הרבה פחות מפחיד.", files_items, n)

    commands_items = [
        item("node -v", "בדיקת גרסת Node", "מציגה אם Node מותקנת ואיזו גרסה קיימת.", "אחרי התקנה או כאשר פקודת Node אינה עובדת.", "הפקודה קבועה; לא מכניסים לתוכה שם משלנו.", "node -v"),
        item("npm -v", "בדיקת גרסת npm", "מציגה את גרסת npm.", "אחרי התקנת Node.", "הפקודה קבועה.", "npm -v"),
        item("npm init", "התחלת פרויקט npm", "שואלת שאלות ויוצרת package.json בתיקייה הנוכחית.", "פעם אחת בתחילת פרויקט חדש.", "npm init קבוע; התשובות לשאלות נבחרות.", "npm init"),
        item("npm install", "התקנת כל החבילות", "קוראת את package.json ומתקינה את התלויות לתוך node_modules.", "אחרי clone או כאשר node_modules חסרה.", "הפקודה קבועה.", "npm install"),
        item("npm install package", "התקנת חבילה מסוימת", "מתקינה חבילה ומוסיפה אותה ל־package.json.", "כאשר הפרויקט צריך ספרייה חדשה.", "npm install קבוע; package מוחלף בשם החבילה.", "npm install axios"),
        item("npm i", "קיצור של npm install", "אותה פעולה בכתיבה קצרה יותר.", "כאשר רוצים להתקין חבילה או את כל החבילות.", "npm i קבוע; שם החבילה נבחר.", "npm i axios"),
        item("tsc --init", "יצירת tsconfig", "יוצרת קובץ tsconfig.json התחלתי.", "פעם אחת בתחילת פרויקט TypeScript.", "הפקודה קבועה.", "tsc --init"),
        item("tsc", "קומפילציה פעם אחת", "קוראת את tsconfig ומתרגמת את קובצי TypeScript ל־JavaScript.", "כשרוצים לבנות את הקוד פעם אחת.", "הפקודה קבועה.", "tsc"),
        item("tsc --watch", "קומפילציה רציפה", "נשארת פתוחה ומקמפלת מחדש אחרי כל שמירה.", "בזמן תרגול ועבודה שוטפת.", "tsc ו־--watch קבועים.", "tsc --watch"),
        item("npm run compile", "הרצת קיצור בשם compile", "npm מחפשת את compile בתוך scripts ב־package.json ומריצה את הפקודה ששמורה שם.", "כאשר הוגדר script בשם compile.", "npm run קבוע; compile הוא שם שהמתכנת בחר.", "npm run compile"),
        item("Current directory", "התיקייה שבה הטרמינל עומד", "כל פקודה פועלת ביחס לתיקייה הנוכחית.", "לפני npm init, npm install או tsc צריך לוודא שאנחנו בתיקיית הפרויקט הנכונה.", "זה מושג; הנתיב משתנה לפי המחשב."),
        item("cd", "מעבר תיקייה בטרמינל", "משנה את התיקייה הנוכחית.", "כאשר צריך להיכנס לפרויקט או ל־src.", "cd קבוע; הנתיב אחריו נבחר.", "cd src"),
    ]
    n = add_category(doc, "חלק ה׳ — פקודות הטרמינל", "את הפקודות האלה מקלידים בטרמינל, לא בתוך קובץ JavaScript או TypeScript.", commands_items, n)

    git_ai_items = [
        item("Git", "מערכת ניהול גרסאות", "שומרת היסטוריה של שינויים בקוד ומאפשרת לעבוד יחד.", "בכל פרויקט כדי לתעד ולסנכרן שינויים.", "Git הוא שם הכלי; שמות commits ו־branches נבחרים."),
        item("GitHub", "אתר לאחסון מאגרי Git", "מקום מרוחק שבו נשמר ה־Repository ואפשר לשתף אותו.", "כדי להעלות, להוריד ולשתף קוד.", "זה שם השירות, לא פקודת קוד."),
        item("Repository / Repo", "מאגר", "תיקיית פרויקט יחד עם היסטוריית Git שלה.", "כאשר עובדים על קוד שמנוהל ב־Git.", "זה מושג; שם ה־Repo נבחר."),
        item("Clone", "הורדת עותק ראשון", "מעתיק Repository מרוחק למחשב ויוצר חיבור אליו.", "פעם ראשונה שמקבלים פרויקט קיים.", "git clone קבוע; הכתובת נבחרת.", "git clone https://github.com/user/repo.git"),
        item("Pull", "משיכת עדכונים", "מוריד ומחבר למחשב את השינויים החדשים מה־Repository המרוחק.", "לפני עבודה או כאשר המרצה העלה חומר חדש.", "git pull קבוע.", "git pull"),
        item("Commit", "נקודת שמירה מתועדת", "אוסף שינויים ונותן להם הודעה המתארת מה נעשה.", "אחרי שסיימנו שינוי ברור ועובד.", "git commit -m קבוע; ההודעה נבחרת.", "git commit -m \"add TypeScript exercise\""),
        item("Push", "העלאת commits", "מעלה את נקודות השמירה מהמחשב ל־GitHub.", "אחרי commit כשרוצים לשתף או לגבות.", "git push קבוע.", "git push"),
        item("Branch", "ענף עבודה", "קו עבודה נפרד שאפשר לשנות בו בלי לגעת מיד ב־main.", "כאשר מפתחים שינוי בנפרד.", "branch הוא מושג; שם הענף נבחר."),
        item("Merge", "מיזוג", "חיבור שינויים מענף אחד לענף אחר.", "אחרי שסיימו עבודה בענף ורוצים לצרף אותה.", "git merge קבוע; שם הענף נבחר."),
        item("Diff", "הבדל בין גרסאות", "מציג אילו שורות נוספו, נמחקו או השתנו.", "לפני commit או בזמן review.", "git diff קבוע.", "git diff"),
        item("Conflict", "התנגשות", "שני שינויים שונים נגעו באותו מקום ו־Git לא יודע לבד במה לבחור.", "בזמן merge או pull כאשר צריך להחליט ידנית.", "זה מושג, לא פקודה יחידה."),
        item("Cursor", "עורך קוד עם כלי AI", "סביבת עבודה דומה ל־VS Code שמאפשרת לשאול AI ולתת לו לבצע שינויים.", "כאשר לומדים, מתכננים או משנים פרויקט בעזרת AI.", "זה שם התוכנה."),
        item("Prompt", "הבקשה ל־AI", "הטקסט שאנחנו כותבים כדי להסביר מה אנחנו רוצים.", "בכל שיחה או משימה מול AI.", "זה מושג; תוכן הבקשה נבחר על ידינו."),
        item("Context", "המידע שה־AI רואה", "הקבצים, הקוד וההודעות שעליהם ה־AI מבסס את התשובה.", "כאשר רוצים תשובה שמתאימה באמת לפרויקט.", "זה מושג. אנחנו בוחרים אילו קבצים לצרף."),
        item("Token", "יחידת טקסט של מודל AI", "המודל קורא וכותב טקסט ביחידות קטנות; ככל שההקשר ארוך יותר משתמשים ביותר tokens.", "כדי להבין מגבלות אורך ועלות של מודל.", "זה מושג, לא פקודה."),
        item("Model", "מודל ה־AI", "המנוע שמייצר תשובות וקוד.", "כאשר בוחרים איזה AI לבצע משימה.", "זה מושג; שם המודל משתנה.", warning="גל המליץ לא לקפוץ בין מודלים אקראיים באמצע פרויקט בלי סיבה."),
        item("Ask mode", "מצב שאלות", "ה־AI מסביר ומייעץ בלי לבצע שינוי גדול בקבצים.", "כשרוצים להבין קוד או לבדוק רעיון.", "Ask הוא שם מצב בכלי."),
        item("Plan mode", "מצב תכנון", "ה־AI בונה תוכנית עבודה לפני שמבצע.", "לפני משימה גדולה או שינוי בכמה קבצים.", "Plan הוא שם מצב.", warning="גל הדגיש לתכנן לפני שנותנים ל־Agent לבצע שינוי גדול."),
        item("Agent mode", "מצב ביצוע", "ה־AI יכול לקרוא קבצים, לערוך ולהריץ פקודות.", "אחרי שהדרישה והתוכנית ברורות.", "Agent הוא שם מצב. עדיין חייבים לבדוק ולהבין את התוצאה."),
        item("Rule", "כלל קבוע ל־AI בפרויקט", "הוראה שנשמרת בפרויקט ומנחה את ה־AI בכל עבודה מתאימה.", "למשל כלל שמפריד HTML, CSS ו־JS.", "Rule הוא מושג; תוכן הכלל נכתב לפי הצורך."),
        item("Skill", "תהליך עבודה חוזר ל־AI", "הוראות מסודרות לביצוע משימה שחוזרת שוב ושוב.", "למשל סדר קבוע לבדיקות או להעלאה ל־Git.", "Skill הוא מושג; שם ותוכן ה־Skill נבחרים."),
        item("Review", "בדיקת קוד", "מבקשים לעבור על הקוד ולמצוא בעיות או אי־התאמות.", "אחרי כתיבה או המרה מ־JS ל־TS.", "זו פעולה/בקשה לכלי AI; הקבצים שנבדקים נבחרים."),
    ]
    n = add_category(doc, "חלק ו׳ — Git וכלי AI", "המילים האלה מתארות את דרך העבודה החדשה של גל. הן אינן כולן פקודות JavaScript.", git_ai_items, n)

    modern_js_items = [
        item("ECMAScript", "התקן של JavaScript", "השם הרשמי של המפרט שמגדיר איך JavaScript עובדת.", "כאשר מדברים על גרסאות וסגנון JavaScript מודרני.", "זה מושג, לא פקודה."),
        item("Arrow function =>", "פונקציית חץ", "דרך קצרה לכתוב פונקציה.", "כאשר רוצים לשמור פונקציה במשתנה או להעביר אותה כערך.", "=> קבוע; שם המשתנה והפרמטרים נבחרים.", "const getUserName = (user: UserSystem) => user.name;"),
        item("Template literal", "מחרוזת עם backticks", "טקסט בין ` ` שבתוכו אפשר לשלב ערכים באמצעות ${}.", "כאשר בונים הודעה עם משתנים.", "ה־backticks ו־${} קבועים; הטקסט ושם המשתנה נבחרים.", "return `sku_${id}`;"),
        item("Destructuring", "פירוק ערכים", "לקיחת שדות מאובייקט או איברים ממערך לתוך משתנים נפרדים.", "כאשר צריך כמה שדות מאותו אובייקט.", "הסוגריים והמבנה קבועים; שמות השדות תלויים באובייקט.", "const { name, email } = employee;"),
        item("Optional chaining ?.", "גישה בטוחה לשדה", "אם החלק שלפני ?. חסר, מתקבל undefined במקום שגיאה.", "כאשר אובייקט או שדה עלולים לא להיות קיימים.", "?. קבוע; שמות האובייקט והשדה נבחרים.", "employee.address?.city"),
        item("Nullish coalescing ??", "ערך חלופי כשאין ערך", "משתמש בערך הימני רק אם השמאלי הוא null או undefined.", "כאשר רוצים ברירת מחדל בלי להחליף 0 או מחרוזת ריקה.", "?? קבוע; שני הערכים נבחרים.", "const phone = employee.phone ?? \"No phone\";"),
        item("querySelector", "חיפוש אלמנט לפי selector", "מחפש את האלמנט הראשון שמתאים ל־CSS selector.", "כאשר רוצים למצוא אלמנט ב־DOM לפי id, class או tag.", "querySelector קבוע; ה־selector בתוך המירכאות נבחר.", "document.querySelector('#title')"),
        item("querySelectorAll", "חיפוש כל האלמנטים", "מחזיר אוסף של כל האלמנטים שמתאימים ל־selector.", "כאשר רוצים לעבור על כמה אלמנטים.", "querySelectorAll קבוע; ה־selector נבחר.", "document.querySelectorAll('.card')"),
        item("createElement", "יצירת אלמנט HTML ב־JS", "יוצר אלמנט חדש בזיכרון לפני שמכניסים אותו לדף.", "כאשר בונים תצוגה דינמית לפי שיטת גל.", "createElement קבוע; שם התג נבחר.", "const row = document.createElement('tr');"),
        item("textContent", "טקסט בתוך אלמנט", "מכניס או קורא טקסט רגיל בלי לפרש אותו כ־HTML.", "כאשר רוצים להציג טקסט בבטחה.", "textContent קבוע; הערך נבחר.", "cell.textContent = product.name;"),
        item("append / prepend", "הוספה לסוף / להתחלה", "מכניסים אלמנט ילד לתוך אלמנט אחר.", "אחרי createElement כדי להוסיף את האלמנט ל־DOM.", "append ו־prepend קבועים; האלמנטים נבחרים.", "tableBody.append(row);"),
        item("DocumentFragment", "מיכל זמני לאלמנטים", "אוספים כמה אלמנטים מחוץ לדף ואז מוסיפים את כולם יחד.", "כאשר בונים הרבה שורות ורוצים לעדכן את ה־DOM בפעם אחת.", "DocumentFragment הוא API מובנה.", "const fragment = document.createDocumentFragment();"),
        item("new Date()", "יצירת תאריך ושעה", "יוצר אובייקט Date של הזמן הנוכחי.", "כאשר שומרים או מציגים מתי פעולה קרתה.", "new ו־Date קבועים.", "const now = new Date();"),
        item("toLocaleString()", "תאריך בפורמט מקומי", "מציג Date לפי השפה והאזור של הדפדפן.", "לתצוגה נוחה למשתמש.", "שם המתודה קבוע.", "now.toLocaleString()"),
        item("toISOString()", "תאריך בפורמט ISO/UTC", "מחזיר טקסט אחיד של זמן לפי UTC.", "לשמירה במסד נתונים או להעברת זמן בצורה אחידה.", "שם המתודה קבוע.", "now.toISOString()"),
        item("Debugging", "איתור תקלה", "עצירה, בדיקה והבנה של מה הקוד עושה בפועל.", "כאשר התוצאה שגויה או הקוד נעצר.", "זה תהליך, לא פקודה אחת."),
        item("Breakpoint", "נקודת עצירה", "סימון שורה שבה הדפדפן עוצר את ריצת הקוד.", "כדי לבדוק ערכי משתנים צעד אחר צעד.", "זה כלי Debugger, לא קוד JavaScript."),
        item("Scope", "תחום גישה", "קובע מאיפה בקוד אפשר לראות משתנה.", "כאשר משתנה זמין בתוך פונקציה או בלוק אבל לא מחוץ להם.", "זה מושג. const ו־let הם בעלי block scope."),
        item("Inline code", "קוד בתוך HTML", "JavaScript או CSS שנכתבים ישירות בתוך תגית HTML.", "רק אם הדרישה מתירה; בשיטת גל לפרויקט הזה מפרידים קבצים.", "זה מושג.", warning="ב־Rule של גל כתוב להפריד HTML, CSS ו־JS ולא לכתוב קוד inline."),
        item("render / init", "שמות נפוצים שהמתכנת בוחר", "render בדרך כלל מציגה מידע; init בדרך כלל מתחילה את התוכנית. אלה אינם פקודות JavaScript.", "כאשר המתכנת בוחר שמות ברורים לפונקציות.", "השמות נבחרים ואפשר להחליפם, כל עוד מעדכנים את הקריאות.", "function init() { render(); }"),
        item("@deprecated", "סימון שפונקציה ישנה", "הערת תיעוד שאומרת שלא מומלץ להשתמש בפונקציה ויש חלופה חדשה.", "כאשר מתחזקים API או קוד ישן.", "@deprecated הוא תג תיעוד קבוע; ההסבר נבחר.", "/** @deprecated Use newFunction() instead. */", "המושג הופיע ב־dummy.ts כהדגמה. הוא אינו חלק מדרישת תרגילי ה־Primitive Types."),
    ]
    n = add_category(doc, "חלק ז׳ — JavaScript מודרני, DOM ו־Debugging", "חלק מהמושגים הופיעו בשיעור כלי ה־AI ובכללי Cursor של גל. הם מסבירים את סגנון הקוד החדש.", modern_js_items, n)

    add_heading(doc, "חלק ח׳ — מה גל ביקש לעשות ומה לא לעשות", 1)
    rules = [
        ("חובה", "בתרגיל JS ל־TypeScript: להשאיר את אותה לוגיקה ורק להוסיף טיפוסים."),
        ("חובה", "לתת טיפוס לפרמטרים, לערכי החזרה ולמשתנים בעלי שם, לפי דרישת התרגיל."),
        ("אסור בשלב הראשון", "לא להוסיף interface, type alias או Object Types לתרגילי ה־Primitive Types."),
        ("חובה", "לקמפל עם tsc עד שאין שגיאות, ואז לוודא שהפלט נשאר זהה ל־JavaScript המקורי."),
        ("מועדף", "לכתוב TypeScript בתוך src ולהוציא JavaScript שנוצר אל dist."),
        ("אסור", "לא לערוך ידנית את קובצי JavaScript שנוצרו ב־dist ולא את הקבצים בתוך node_modules."),
        ("לא מומלץ", "לא להשתמש ב־any בדרך כלל, מפני שהוא מבטל את בדיקת הטיפוסים."),
        ("חשוב", "בדיקת TypeScript היא לפני הריצה; היא אינה מחליפה Validation של מידע אמיתי בזמן ריצה."),
        ("חשוב", "as אינו Validation ואינו יוצר מידע חסר. הדוגמה return {} as Company הייתה הדגמה בלבד."),
        ("שיטת עבודה", "ה־Repository וה־README הם מקור האמת לחומר ולהוראות."),
        ("שיטת עבודה", "לתכנן לפני שמפעילים Agent על שינוי גדול, ולקרוא ולבדוק את הקוד שה־AI יצר."),
        ("שיטת קוד", "להפריד HTML, CSS ו־JavaScript; לא להשתמש בקוד inline לפי ה־Rule של גל."),
        ("שינוי מהעבר", "אצל גל מועדפים querySelector/createElement/addEventListener. זה שונה מסגנון מבחן שחר שבו הועדפו getElementById/innerHTML/onsubmit."),
    ]
    add_table(doc, ["רמת הכלל", "ההוראה בפשטות"], rules, [2100, 7260])

    add_heading(doc, "Workflow אחד שמחבר את הכול", 1)
    workflow = [
        ("1", "נכנסים בטרמינל לתיקיית הפרויקט הנכונה."),
        ("2", "אם זה פרויקט קיים: npm install. אם חדש: npm init."),
        ("3", "כותבים TypeScript ב־src ומוסיפים טיפוסים לפי הדרישה."),
        ("4", "מריצים tsc או npm run compile."),
        ("5", "TypeScript בודקת שגיאות ויוצרת JavaScript ב־dist."),
        ("6", "ה־HTML טוען את dist/index.js או dist/shop.js — לא את קובץ ה־.ts."),
        ("7", "מריצים ובודקים שההתנהגות והפלט נכונים."),
        ("8", "בודקים git diff, מבצעים commit, ואז push כשמוכנים לשתף."),
    ]
    add_table(doc, ["שלב", "מה עושים"], workflow, [1100, 8260])

    add_heading(doc, "דוגמה שלמה קצרה מהשיעור", 1)
    add_code(doc, "function calcSubtotal(unitPrice: number, quantity: number): number {\n  return unitPrice * quantity;\n}\n\nconst subtotal: number = calcSubtotal(19.9, 3);")
    add_text(doc, "פירוק:", bold=True, after=3)
    for line in (
        "function, return, הסוגריים והסוגריים המסולסלים — תחביר קבוע.",
        "calcSubtotal, unitPrice, quantity ו־subtotal — שמות שהמתכנת בחר.",
        ": number — בדיקת TypeScript: הפרמטר או התוצאה חייבים להיות מספר.",
        "19.9 ו־3 — ערכים שהמתכנת הכניס.",
        "* — פעולת כפל של JavaScript.",
    ):
        add_text(doc, line, after=2)

    add_heading(doc, "אינדקס מהיר — איפה לחפש כל מילה", 1)
    index_rows = [
        ("TypeScript", "א׳", "שפה עם בדיקת טיפוסים"),
        ("string / number / boolean / any", "א׳", "טיפוסים בסיסיים"),
        ("parameter / return / void", "ב׳", "טיפוסים בפונקציה"),
        ("type alias / union / intersection / optional", "ב׳", "טיפוסים מותאמים"),
        ("typeof / ReturnType / as", "ב׳", "כלי טיפוסים מתקדמים"),
        ("Node / npm / dependency / Axios", "ג׳", "סביבת עבודה וחבילות"),
        ("package.json / tsconfig / src / dist", "ד׳", "מבנה הפרויקט"),
        ("npm install / tsc / npm run", "ה׳", "פקודות טרמינל"),
        ("Git / clone / pull / commit / push", "ו׳", "ניהול גרסאות"),
        ("Prompt / Context / Plan / Agent / Rule", "ו׳", "כלי AI"),
        ("Arrow / Template literal / DOM", "ז׳", "JavaScript מודרני"),
        ("Debugging / Breakpoint / Scope", "ז׳", "איתור תקלות"),
    ]
    add_table(doc, ["מה מחפשים", "חלק", "הקבוצה"], index_rows, [4500, 1100, 3760])

    add_heading(doc, "מקורות שנבדקו", 1)
    sources = [
        "מאגר גל FS_AI_45800_9, תיקיות 30-8-AI-Tools ו־02-9-Typescript, מעודכן עד commit 9697d41 מ־02.09.2026.",
        "README הראשי ו־02-9-Typescript/readme.md.",
        "קוד השיעור: lab_1/src/index.ts, lab_2/src/shop.ts, lab_2/src/type_alias.ts, dummy.ts וקובצי התרגילים.",
        "תמלול מלא של שיעור 02.09.2026: TYPESCRIPT-ESSENTIALS-2026-09-02-full-transcript.txt.",
        "מדריכי השיעור L-2026-08-30 ו־L-2026-09-02 במאגר הלימוד האישי.",
    ]
    for source in sources:
        add_text(doc, f"• {source}", size=9.5, color=MID_GRAY, after=3)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    build_document()
