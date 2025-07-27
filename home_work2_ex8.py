"""
קבל מהמשתמש את הגיל ואת משקלו בק"ג.8
אם הגיל קטן מ-12, המינון הוא 10 מ"ג לכל ק"ג גוף.
אם הגיל בין 12 ל-65, המינון הוא 500 מ"ג קבוע.
אם הגיל מעל 65, המינון הוא 250 מ"ג.
הדפס את המינון המומלץ בהתאם

"""
age = float(input("please enter your age:"))
weight = float(input("please enter your weight:"))
between_12_to_65_dose = 500
over_65_dose = "250 mg"
new_dose = f"your dose:{between_12_to_65_dose} mg"
if age < 12:
    print(f"your dose :{10 * weight}")
elif 12 < age < 65:
    print(f"your dose:{between_12_to_65_dose} mg")
else:
    print(f"your dose :{over_65_dose}")
