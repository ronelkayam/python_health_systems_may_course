"""
קבל גיל מהמשתמש
 וענה על השאלה: "האם אתה סובל ממחלה כרונית?" (כן/לא)
אם הגיל מעל 65 או יש מחלה כרונית, הדפס "מומלץ להתחסן נגד שפעת".
אחרת, הדפס "החיסון אינו חובה אך מומלץ".

"""
age = float(input("please enter your age:"))
print(f"your age is:{age}")
chronic_illness = input("Do you suffer from a chronic illness? (yes/no)")
if chronic_illness != "yes" and chronic_illness != "no":
    print("wrong answer!!!!")
else:
    if age > 65 or chronic_illness == "yes":
        print("recommended to get vaccinated against the flu!")
    else:
        print("vaccinated is not required!")


