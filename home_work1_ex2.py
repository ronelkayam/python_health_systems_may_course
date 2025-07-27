"""
•	בקש מהמשתמש להזין משקל בקילוגרמים וגובה במטרים.
•	חשב את מדד ה-BMI לפי הנוסחה:
BMI = משקל / (גובה ** 2)
•	הדפס את התוצאה.

"""
weight = float(input("please enter your weight:"))
high = float(input("please enter your high:"))
bmi = weight / (high ** 2)
int_bmi = weight // (high ** 2)
#round fumction get 2 arguments - first number, second number after point
round_bmi = round(weight/(high**2),3)
print(f"your bmi :{bmi}")
print(f"round bmi:{round_bmi}")
print(f"your bmi:{weight / (high ** 2)}")
print(f"your weight:{weight}, your high:{high} your BMI:{round_bmi}")
