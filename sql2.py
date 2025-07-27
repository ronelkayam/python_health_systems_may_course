import sqlite3

# התחברות למסד נתונים (אם הקובץ לא קיים, הוא ייווצר)
conn = sqlite3.connect('my_database.db')

# יצירת סמן להרצת שאילתות
cursor = conn.cursor()

# יצירת טבלה
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# הוספת נתונים
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("מוחמד", 95))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("גל",35))
conn.commit()  # חשוב לשמור שינויים

# שליפת נתונים

# שליפת נתונים
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()


cursor.execute("SELECT * FROM users where age>60")
rows_bigger_60 = cursor.fetchall()



# הצגת התוצאות
print("all users")
for user in all_users:
    print(f"ID: {user[0]}, שם: {user[1]}, גיל: {user[2]}")

print("רשימת משתמשים מבוגרים מגיל 60:")
for row in rows_bigger_60:
    print(f"ID: {row[0]}, שם: {row[1]}, גיל: {row[2]}")

# סגירת החיבור
conn.close()
