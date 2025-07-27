"""
1.	צור רשימה של מטופלים עם 8 שמות
א. הדפס את המטופל הראשון ברשימה
ב. הוסף את השם sara לרשימה
ג. הדפיסו את אורך הרשימה
ד. עברו על הרשימה והדפיסו את הרשימה עם משפט מתאים של קבלת תור.
ה. מיינו את הרשימה עם 2 השיטות והדפיסו.

"""
patients_count = 8
patient_ls = []
for patient in range(patients_count):
    # name = input("please enter patient name:")
    # patient_ls.append(name)
    patient_ls.append(input("please enter patient name:"))
for patient in patient_ls:
    print(patient)
print(f"first patient is:{patient_ls[0]}")
print(f"before append:{patient_ls}")
patient_ls.append("sara")
print(f"after append:{patient_ls}")
length = len(patient_ls)
print(f"patients list length are:{length}")
# print(f"patients list length are:{len(patient_ls)}")
for patient in patient_ls:
    print(f"patient name is:{patient}, you are the next in line!")
# 1 opt
print("*****first option to sorting*****")
print(f"before sort:{patient_ls}")
sort_patient_ls = sorted(patient_ls)
print(f"patient_ls:{patient_ls}")
print(f"sort patient ls=:{sort_patient_ls}")

# 2 opt
print("**************second option to sorting*****************")
print(f"before sort:{patient_ls}")
print(f"after sort:{patient_ls.sort()}")
print(f"reverse sort :{patient_ls.sort(reverse=True)}")
