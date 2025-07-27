"""
קלוט את מס' החדרים במרפאה
 וכתוב לולאה שמבקשת לקלוט שם רופא
 ומדפיסה את מספרי החדרים במרפאה ולידם שם הד"ר המטפל.
"""
rooms_count = int(input("please enter count of room numbers in hospital:"))
print(f"Room count in hospital:{rooms_count}")
for room_number in range(1, rooms_count + 1):
    doctor_name = input("Hello doctor, please enter your name:")
    print(f"Room number:{room_number}, doctor:{doctor_name}")
print("Thank you and good bye")
