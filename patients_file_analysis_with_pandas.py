import pandas as pd
from collections import Counter

# Read the CSV file
df = pd.read_csv('patients.csv')

# Exercise 1: Print all patients
print("\n--- Exercise 1: Print all patients ---")
print(df)

# Exercise 2: Count of each medical condition
print("\n--- Exercise 2: Count of each medical condition ---")
print(df['מצב רפואי'].value_counts())

# Exercise 3: Patients aged 65+
print("\n--- Exercise 3: Patients aged 65+ ---")
print(df[df['גיל'] >= 65])

# Exercise 4: Unique patient names
print("\n--- Exercise 4: Unique patient names ---")
print(df['שם'].unique())

# Exercise 5: Duplicate names
print("\n--- Exercise 5: Names that appear more than once ---")
print(df['שם'].value_counts()[df['שם'].value_counts() > 1])

# Exercise 6: Who needs a medical checkup
print("\n--- Exercise 6: Patients who need a checkup ---")
checkup_conditions = ['סוכרת', 'לחץ דם גבוה', 'מחלה כרונית']
needs_checkup = df[(df['גיל'] >= 40) | (df['מצב רפואי'].isin(checkup_conditions))]
print(needs_checkup[['שם']])

# Exercise 7: Save checkup list to file
print("\n--- Exercise 7: Saving checkup list to file ---")
needs_checkup.to_csv('checkup_needed.csv', index=False)
print("Saved to: checkup_needed.csv")

# Exercise 8: Average age by medical condition
print("\n--- Exercise 8: Average age by medical condition ---")
print(df.groupby('מצב רפואי')['גיל'].mean().round(1))

# Exercise 9: Search by name
print("\n--- Exercise 9: Search for a patient by name ---")
query = input("Enter name to search: ").strip()
results = df[df['שם'].str.contains(query, na=False)]
if results.empty:
    print("Name not found")
else:
    print(results)

# Exercise 10: Most common first name
print("\n--- Exercise 10: Most common first name ---")
first_names = df['שם'].dropna().apply(lambda x: x.split()[0])
most_common = Counter(first_names).most_common(1)[0]
print(f"The most common first name is: {most_common[0]} ({most_common[1]} times)")
