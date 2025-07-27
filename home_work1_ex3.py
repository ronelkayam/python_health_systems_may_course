"""
•	בקש מהמשתמש להזין את שנת הלידה שלו.
•	חשב את גילו על פי השנה הנוכחית (למשל 2025).
•	הדפס:
גילך הוא: <גיל> שנים.

"""
local_year = 2025
birth_year = int(input("please enter your birth year:"))
age = local_year-birth_year
print(f"your age is:{age}")
print(f"your local year:{local_year}, your birth year:{birth_year}, your age is:{age}")

