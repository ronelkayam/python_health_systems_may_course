"""
במשך 7 ימים, מטופל מקבל תרופה.
 כל יום יש להכניס את המינון היומי (input),
 ובסיום לחשב ולדווח מה הייתה המנה המצטברת לכל השבוע
"""
# days = 7
# sum_dose = 0
# for day in range(days):
#     sum_dose += int(input("please enter day dose:"))
# print(f"all :{days} dose:{sum_dose}")

days = 7
sum_dose = 0
for day in range(days):
    dose = int(input("please enter day dose:"))
    sum_dose += dose
print(f"all :{days} dose:{sum_dose}")
