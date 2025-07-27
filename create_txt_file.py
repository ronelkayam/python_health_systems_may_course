# the 'w' flag is for writing
with open('./text.txt', 'w', encoding='utf-8') as f:
    f.write('שלום מסמכי פייתון')

"""
אם הקובץ לא קיים, פייתון ייצור אותו.
אנחנו מצפים מהקובץ להיות באותה תיקייה כמו הסקריפט של פייתון.
המוד w יגרום לפייתון לכתוב לקובץ מתחילתו.
קידוד utf-8 הוא מאוד חשוב כשעובדים עם שפות אקזוטיות דוגמת עברית.
אם כבר פתחנו את הקובץ אפשר לכתוב לתוכו כמה פעמים שרוצים.
"""

with open('./text.txt', 'w', encoding='utf-8') as f:
    f.write('שלום ')
    f.write(' מסמכי')
    f.write(' פייתון')
# לאן נעלם התוכן הקודם שהיה רשום לתוך הקובץ? הוא נמחק על ידי הסקריפט
# כיוון ששימוש במוד w מוחק את כל מה שהיה בקובץ, ואז מתחיל לכתוב את הקובץ מתחילתו.
cars = ['BMW', 'Audi', 'Ferrari', 'Tesla', 'Jaguar']

with open('./text.txt', mode='w', encoding='utf-8') as f:
    for car in cars:
        # \n is the new line character
        f.write(car + "\n")

# לצורך קריאת הקובץ נשתמש במוד r (קיצור של read):
# Here it reads the entire file
with open('./text.txt', 'r', encoding='utf-8') as f:
    f_contents = f.read()
    print(f_contents)


"""
הקובץ text.txt נמצא באותה התיקייה כמו הסקריפט
מוד r אחראי לפתיחת הקובץ לקריאה
הפונקציה f.read() קוראת את כל תוכנו של הקובץ בבת אחת
כפי שניתן לקרוא את כל תוכנו של הקובץ באמצעות הפונקציה f.read() הפונקציה f.readlines() הופכת את תוכנו של הקובץ למערך כשכל שורה חדשה הופכת לפריט במערך.
"""
with open('./text.txt', 'r', encoding='utf-8') as f:
    print(f.readlines())


#הפונקציה readline()
# קוראת שורה אחת בלבד בכל פעם שקוראים לה. הקוד הבא קורא את ה-3 שורות הראשונות של הקובץ:

with open('./text.txt', 'r', encoding='utf-8') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

#כדי לקרוא קובץ שלם שורה אחר שורה. מה שמאפשר לנו לקרוא מסמכים ארוכים במיוחד נשתמש בלולאת for.
with open('./text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='#NEW LINE#')


#ניתן לקבוע מה יהיה אורך התווים שנקרא בכל פעם. במקרה זה נגביל ל-3 תווים בלבד בכל פעם.
with open('./text.txt', 'r', encoding='utf-8') as f:
    f_content = f.read(3)  # first 3 characters
    print(f_content)

    f_content = f.read(3)  # next 3 characters
    print(f_content)

"""
בפעם הראשונה שהקוד רץ הוא מדפיס את שלושת התווים הראשונים במסמך, BMW.
בפעם השנייה שהקוד רץ הוא מדפיס את שלושת התווים הבאים בתור, שורה חדשה ואח"כ Au.
כשמספר התווים במסמך גדול מדי נשתמש בלולאת while
 שרצה בכל פעם מספר נתון של תווים עד שהיא מגיעה לסופו של הקובץ כדי למנוע הצפה של זיכרון המחשב.
"""
with open('./text.txt', 'r', encoding='utf-8') as f:
    len_to_read = 3

    f_content = f.read(len_to_read)

    while len(f_content) > 0:
        print(f_content, end='*')
        f_content = f.read(len_to_read)