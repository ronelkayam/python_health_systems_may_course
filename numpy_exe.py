"""
צור מערך NumPy בגודל 1000 עם ערכים אקראיים של רמות סוכר בדם בטווח 70–200.
חשב ממוצע, חציון וסטיית תקן.
כמה ערכים חורגים מהטווח התקני (נניח 80–140)?
"""
import numpy as np

print("****************ex1******************")
# create list with 1000 values between 70-200
blood_suger = np.random.randint(70, 200, size=1000)
print(blood_suger.size)

mean = np.mean(blood_suger)
median = np.median(blood_suger)
std_dev = np.std(blood_suger)
out_of_range = np.sum((blood_suger < 80) | (blood_suger > 140))

print(f"avg:{mean}")
print(f"median:{median}")
print(f"std:{round(std_dev, 2)}")
print(f"sum out of range 80-140:{out_of_range}")

"""
 תרגיל: ניתוח נתוני לחץ דם סיסטולי של מטופלים
יש לך רשימה של ערכי לחץ דם סיסטולי (המספר הגבוה יותר במדידה) של 10 מטופלים.
 כתוב קוד ב-NumPy שמבצע את הפעולות הבאות:
יצירת מערך NumPy מתוך הנתונים.
חישוב הממוצע, החציון וסטיית התקן.
זיהוי מטופלים שערך לחץ הדם שלהם גבוה מהממוצע ביותר מסטיית תקן אחת.
"""
print("*********************ex2*****************")
pressures = np.array([120, 90, 95, 85, 140, 123, 150, 90, 70, 110])

mean = np.mean(pressures)
median = np.median(pressures)
std_dev = np.std(pressures)

high_pressure = pressures[pressures > mean + std_dev]

print(f"avg:{mean}")
print(f"median:{median}")
print(f"std:{round(std_dev, 2)}")
print(f"high_pressure:{high_pressure}")

"""
בית חולים אוסף מידע על מדדים פיזיולוגיים של מטופלים, כולל לחץ דם סיסטולי, לחץ דם דיאסטולי, דופק, ורמות סוכר. 
כל שורה מייצגת מדדים של מטופל אחד.
חשב ממוצע וסטיית תקן של כל אחד מהמדדים.
חשב את מספר המטופלים עם לחץ דם סיסטולי גבוה מ-140.
מצא את המטופל עם רמת הסוכר הגבוהה ביותר.
נרמל את כל הערכים במדדים (Z-score normalization).
"""

# כל שורה: [לחץ דם סיסטולי, לחץ דם דיאסטולי, דופק, סוכר (mg/dL)]
data = np.array([
    [130, 85, 72, 110],
    [140, 90, 80, 130],
    [125, 82, 75, 105],
    [160, 100, 95, 150],
    [135, 88, 78, 120]
])

mean = np.mean(data, axis=0)
std_dev = np.std(data, axis=0)
print(f"mean:{mean}")
print(f"std:{std_dev}")
systolic_over_140 = data[:, 0] > 140
sum_high_systolic = np.sum(systolic_over_140)
print(f"sum high systolic:{sum_high_systolic}")
max_suger = np.argmax(data[:, 3])
print(f"max suger:{max_suger}")
