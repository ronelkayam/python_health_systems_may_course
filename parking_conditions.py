"""
עליכם לבנות קוד המחשב עלות חניה לפי מספר פרמטרים
הקוד מקבל מהמשתמש נתונים אודות החניה ומציג למשתמש מהו הסכום לתשלום

התעריף לשעת חניה משתנה בהתאם לכמות שעות החניה באופן הבא:

עד 3 שעות – 20 ₪ לשעה
בין 3 ל 5 שעות – 15 ₪ לשעה
בין 5 ל 24 שעות – 10 ₪ לשעה
יותר מ 24 שעות – 5 ₪ לשעה

"""
name = input("please enter your name:")
until_3_hours = 20
between_3_to_5 = 15
between_5_and_24 = 10
over_24 = 5
parking_hours = float(input(f"{name}, please enter your parking hours:"))
if parking_hours <= 3:
    sum = parking_hours * until_3_hours
    print(f"{name}, your bill is:{sum} NIS")
elif parking_hours <= 5:
    sum = parking_hours * between_3_to_5
    # sum = (3*until_3_hours)+((parking_hours -3 )*between_3_to_5)
    print(f"{name}, your bill is:{sum} NIS")
elif parking_hours <= 24:
    sum = parking_hours * between_5_and_24
    print(f"{name}, your bill is:{sum} NIS")
else:
    sum = parking_hours * over_24
    print(f"{name}, your bill is:{sum} NIS")
