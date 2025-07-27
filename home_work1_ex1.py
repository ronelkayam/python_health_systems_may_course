"""
•	בקש מהמשתמש להזין את שמו המלא ואת מספר תעודת הזהות שלו.
•	הדפס הודעת ברכה:
שלום <שם>, מספר מזהה שלך הוא <מספר>.

"""
full_name = input("Full name:")
id = input("Your id:")
line_number = int(input("please enter your line number:"))
print(f"Hello {full_name} , your id is:{id}, your line number is:{line_number}")