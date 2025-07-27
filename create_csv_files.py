import csv
import random
from datetime import datetime, timedelta

# שמות לדוגמה
first_names = ["דנה", "יוסי", "רונית", "אלי", "מיכל", "דוד", "יעל", "ניר", "תמר", "עידן"]
last_names = ["כהן", "לוי", "רוזן", "שמואלי", "גולדשטיין", "פרידמן", "קרן", "בן דוד", "בלוך", "בר"]

conditions = ["בריא/ה", "סוכרת", "לחץ דם גבוה", "אסטמה", "כולסטרול", "מחלה כרונית"]
statuses = ["בוצע", "בוטל", "עתידי"]

def random_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def random_date(start_days_ago=365, end_days_from_now=365):
    start = datetime.now() - timedelta(days=start_days_ago)
    end = datetime.now() + timedelta(days=end_days_from_now)
    return (start + (end - start) * random.random()).strftime("%Y-%m-%d")

# patients.csv
with open("patients.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["שם", "גיל", "מצב רפואי"])
    for _ in range(50):
        writer.writerow([random_name(), random.randint(18, 90), random.choice(conditions)])

# vaccinations.csv
with open("vaccinations.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["שם", "גיל", "תאריך חיסון"])
    for _ in range(50):
        writer.writerow([random_name(), random.randint(18, 90), random_date()])

# appointments.csv
with open("appointments.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["שם", "תאריך תור", "סטטוס"])
    for _ in range(50):
        writer.writerow([random_name(), random_date(-30, 90), random.choice(statuses)])
