import pandas as pd
import random
from datetime import datetime, timedelta


def create_dummy_patients_csv(filename='patients_for_pandas.csv', num_rows=100):
    names = ['David', 'Sarah', 'John', 'Leah', 'Michael', 'Ruth'
        , 'Daniel', 'Hannah', 'Adam', 'Esther']
    diagnoses = ['Hypertension', 'Diabetes', 'Flu', 'Asthma', 'COVID-19']

    data = []
    base_date = datetime(2025, 1, 1)

    for i in range(1, num_rows + 1):
        patient = {
            'PatientID': i,
            'Name': random.choice(names),
            'Age': random.randint(20, 90),
            'Diagnosis': random.choice(diagnoses),
            'VisitDate': (base_date + timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
        }
        data.append(patient)

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"הקובץ '{filename}' נוצר בהצלחה עם {num_rows} שורות.")


# קריאה לדוגמה
create_dummy_patients_csv()

# קריאת הקובץ
df = pd.read_csv('patients_for_pandas.csv')

# הדפסת הנתונים הראשונים
print("נתונים ראשונים:")
print(df.head())

# פילטר – כל המטופלים עם יתר לחץ דם (Hypertension)
hypertension_patients = df[df['Diagnosis'] == 'Hypertension']
print("\nמטופלים עם יתר לחץ דם:")
print(hypertension_patients)

# ממוצע גיל לפי אבחנה
avg_age_by_diagnosis = df.groupby('Diagnosis')['Age'].mean()
print("\nממוצע גיל לפי אבחנה:")
print(avg_age_by_diagnosis)

# המרת העמודה VisitDate לפורמט תאריך
df['VisitDate'] = pd.to_datetime(df['VisitDate'])

# סינון ביקורים שהיו אחרי תאריך מסוים
recent_visits = df[df['VisitDate'] > '2025-06-02']
print("\nביקורים אחרי 2025-06-02:")
print(recent_visits)
