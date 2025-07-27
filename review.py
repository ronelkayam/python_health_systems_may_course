# הדפס את כל המספרים מ1 עד 10
for i in range(1, 11):
    print(i, end=' ')  # stay same line
print()
print("printing another line")

# כתוב תכנית שמדפיסה את סכום כל המספרים מ1 עד 100
sum = 0
for i in range(1, 101):
    sum += i
print(f" sum of 1-100 {sum}")

"""
קלוט מהמשתמש כתובת מייל והחזר אם תקינה או לא
תקינות של כתובת מייל
פעם אחת בלבד חובה @
פעם אחת .com 
פעם אחת .
"""
mail = input("please enter your mail:")
print(f"mail:{mail}")
# ronelk6@gmail.com
count_shtrodel = 0
count_point = 0
for i in mail:
    if i == '@':
        count_shtrodel += 1
    elif i == '.':
        count_point += 1
if count_shtrodel == 1 and count_point == 1 and ".com" in mail:
    print(f"mail:{mail} is legal")
else:
    print(f"mail:{mail} is illegal")

# קלטו מחרוזת בעלת 20 תווים,
# בידקו שזה האורך
# והדפיסו כמה פעמים מופיע התו '!'

new_str = input("please enter 20 chars:")
str_length = len(new_str)
count = new_str.count("!")
print(f"length of string:{str_length}")
print(f"{count} times appear ! in {new_str}")

# קלטו מספרים עד שיקלט -1 , הדפיסו את הכמות
count = 0
num = int(input("please enter number,-1 to stop!"))
while num != -1:
    count += 1
    num = int(input("please enter number,-1 to stop!"))
print(f"count of input numbers:{count}")

# קלטו שמות של רופאים עד שיקלט גרגורי
name = input("hello doctor, please enter your name:")
while name != 'Gregori':
    name = input("hello doctor, please enter your name:")

# הדפיסו את כל המספרים מ1 עד 30 באותה שורה עם לולאת while
i = 1
while i < 30:
    print(i, end=' ')
    i += 1

# הראה רשימה עם פעולות עליה
ls = []
print(ls)
ls.append("ron")  # [ron]
ls.append("moshe")  # [ron,moshe]
ls.append("mohamad")  # [ron,moshe,mohamad]
location_to_add = 2
if len(ls) > location_to_add:
    ls.insert(location_to_add, "david")  # [ron,moshe,david,mohamad]
ls[2] = "bar"  # [ron,moshe,bar,mohamad]
name = "bar"
if name in ls:
    print(ls.index(name))  # 2
location_to_delete = 1
if len(ls) > location_to_delete:
    del ls[location_to_delete]

"""
הגדירו רשימה של ציונים 
הדפיסו את המערך 
וכמות ציונים נכשלים
"""
grades_ls = [100, 45, 90, 85, 60]
print(grades_ls)
# ls = []
# for i in range(5):
#     ls.append(int(input("please enter number:")))
# print(ls)
failed_grades_count = 0
for grade in grades_ls:
    if grade < 61:
        failed_grades_count += 1
print(f"failed grades count in ls:{grades_ls} is:{failed_grades_count}")

# קלטו רשימה של ציונים ווצרו שני רשימות נוספות של ציונים נכשלים ועוברים
grades_ls = []
failed_grades_ls = []
pass_grades_ls = []
for i in range(5):
    grades_ls.append(int(input("please enter grade:")))
    if grades_ls[i] > 60:
        pass_grades_ls.append(grades_ls[i])
    else:
        failed_grades_ls.append(grades_ls[i])

print(f"grades ls:{grades_ls}")
print(f"failed grades ls:{failed_grades_ls}")
print(f"pass grades ls:{pass_grades_ls}")


