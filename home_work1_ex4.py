"""
•	בקש מהמשתמש להזין את טמפרטורת הגוף במעלות צלזיוס.
•	המר אותה לפרנהייט לפי הנוסחה:
F = C * 9/5 + 32
•	הדפס את שתי הטמפרטורות.

"""
celzius = float(input("please enter your body temperature:"))
farenhite = celzius * (9 / 5) + 32
round_f = round(farenhite, 2)
print(f"celizus temp:{celzius}\nfarenhite temp:{round_f}")
