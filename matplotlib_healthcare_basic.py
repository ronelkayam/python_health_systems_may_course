import pandas as pd
import matplotlib.pyplot as plt

# יצירת נתונים לדוגמה
data = {
    'מחלקה': ['פנימית', 'כירורגית', 'ילדים', 'יולדות', 'אורתופדית'],
    'מספר מטופלים': [120, 80, 95, 70, 60]
}

# המרת הנתונים לטבלה (DataFrame)
df = pd.DataFrame(data)

# יצירת גרף עמודות
plt.figure(figsize=(10, 6))
plt.bar(df['מחלקה'], df['מספר מטופלים'], color='skyblue')

# כותרות לגרף
plt.title('מספר מטופלים לפי מחלקה')
plt.xlabel('מחלקה')
plt.ylabel('מספר מטופלים')

# הצגת הגרף
plt.show()
