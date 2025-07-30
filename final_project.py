# פרויקט מסכם - ניתוח נתוני חולי סוכרת (דאטה סינתטית)
"""
This project analyzes synthetic health data to identify patterns related to diabetes.
 It includes data generation, processing,
 statistical analysis, and visualization of key health indicators.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

def main():
    # יצירת דאטה סינתטי
    random.seed(42)
    np.random.seed(42)

    n = 100  # מספר דגימות

    genders = ['Female', 'Male']
    ages = np.random.randint(20, 80, size=n)
    bmi = np.round(np.random.normal(loc=28, scale=6, size=n), 1)
    glucose = np.round(np.random.normal(loc=120, scale=30, size=n))
    outcome = []

    # פונקציה פשוטה לסימון חולי סוכרת לפי BMI וגלוקוז
    for i in range(n):
        risk_score = 0
        risk_score += (bmi[i] > 30) * 1
        risk_score += (glucose[i] > 130) * 1
        risk_score += (ages[i] > 45) * 1
        # סיכוי להיות חולה עולה ככל שיותר תנאים מתקיימים
        outcome.append(1 if risk_score >= 2 else 0)

    gender_col = [random.choice(genders) for _ in range(n)]

    # בניית DataFrame
    df = pd.DataFrame({
        'Gender': gender_col,
        'Age': ages,
        'BMI': bmi,
        'Glucose': glucose,
        'Outcome': outcome
    })

    # הצגת 5 השורות הראשונות
    print("חמש שורות ראשונות:")
    print(df.head())

    # --- ניקוי נתונים ---
    print("\nבדיקת ערכים חסרים:")
    print(df.isnull().sum())

    # במקרה זה אין ערכים חסרים, אך ננקה במידת הצורך
    df = df.dropna(subset=['Age', 'BMI', 'Glucose', 'Outcome'])

    # --- ניתוח נתונים ---
    print("\nכמות חולים ללא חולים:")
    print(df['Outcome'].value_counts())

    print("\nממוצע גיל לפי Outcome:")
    print(df.groupby('Outcome')['Age'].mean())

    print("\nממוצע BMI לפי מגדר:")
    print(df.groupby('Gender')['BMI'].mean())

    # --- ויזואליזציה ---

    # היסטוגרמה של גילאים
    plt.figure(figsize=(8,5))
    plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
    plt.title('התפלגות גילאי המטופלים')
    plt.xlabel('גיל')
    plt.ylabel('מספר מטופלים')
    plt.grid(True)
    plt.show()

    # השוואת BMI בין חולי סוכרת ללא חולים
    plt.figure(figsize=(6,4))
    df.boxplot(column='BMI', by='Outcome')
    plt.title('BMI לפי מצב סוכרת')
    plt.suptitle('')
    plt.xlabel('Outcome (0=ללא, 1=עם)')
    plt.ylabel('BMI')
    plt.show()

    # ממוצע גלוקוז לפי Outcome
    plt.figure(figsize=(6,4))
    df.groupby('Outcome')['Glucose'].mean().plot(kind='bar', color=['green','red'])
    plt.title('ממוצע רמות גלוקוז לפי Outcome')
    plt.xlabel('Outcome (0=ללא, 1=עם)')
    plt.ylabel('רמת גלוקוז ממוצעת')
    plt.grid(axis='y')
    plt.show()

    # --- תובנות ---
    print("\n--- תובנות ---")
    print("- חולי סוכרת נוטים להיות עם BMI גבוה יותר מהממוצע.")
    print("- שכיחות הסוכרת עולה עם הגיל, במיוחד מעל גיל 45.")
    print("- רמות גלוקוז גבוהות קשורות לסיכון מוגבר לסוכרת.")

if __name__ == "__main__":
    main()
