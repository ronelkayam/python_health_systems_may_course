"""
כתוב לולאה שמבקשת שוב ושוב מהמשתמש להכניס ערך (למשל "מדד לחץ דם").
עצור את הלולאה אם הוזן הערך stop , ואז הצג כמה מדדים הוזנו לפני כן.
"""
count = 0
blood_presser = input("please enter your blood presser (stop to exit!):")
while blood_presser != "stop":
    count += 1
    blood_presser = input("please enter your blood presser (stop to exit!):")
print(f"sum of patience :{count}")
