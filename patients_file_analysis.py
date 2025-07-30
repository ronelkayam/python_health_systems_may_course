import csv
from collections import Counter

# Load CSV file manually
with open('patients.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

# Convert numerical fields (like age) to int
for row in data:
    row['גיל'] = int(row['גיל'])

# Exercise 1: Print all patients
print("\n--- Exercise 1: Print all patients ---")
for row in data:
    print(row)

# Exercise 2: Count of each medical condition
print("\n--- Exercise 2: Count of each medical condition ---")
medical_counts = Counter(row['מצב רפואי'] for row in data)
for condition, count in medical_counts.items():
    print(f"{condition}: {count}")

# Exercise 3: Patients aged 65+
print("\n--- Exercise 3: Patients aged 65+ ---")
for row in data:
    if row['גיל'] >= 65:
        print(row)

# Exercise 4: Unique patient names
print("\n--- Exercise 4: Unique patient names ---")
unique_names = set(row['שם'] for row in data)
for name in unique_names:
    print(name)

# Exercise 5: Duplicate names
print("\n--- Exercise 5: Names that appear more than once ---")
name_counts = Counter(row['שם'] for row in data)
for name, count in name_counts.items():
    if count > 1:
        print(f"{name}: {count}")

# Exercise 6: Who needs a medical checkup
print("\n--- Exercise 6: Patients who need a checkup ---")
checkup_conditions = ['סוכרת', 'לחץ דם גבוה', 'מחלה כרונית']
needs_checkup = []
for row in data:
    if row['גיל'] >= 40 or row['מצב רפואי'] in checkup_conditions:
        needs_checkup.append(row)
        print(row['שם'])

# Exercise 7: Save checkup list to file
print("\n--- Exercise 7: Saving checkup list to file ---")
with open('checkup_needed.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(needs_checkup)
print("Saved to: checkup_needed.csv")

# Exercise 8: Average age by medical condition
print("\n--- Exercise 8: Average age by medical condition ---")
condition_ages = {}
for row in data:
    condition = row['מצב רפואי']
    age = row['גיל']
    if condition not in condition_ages:
        condition_ages[condition] = []
    condition_ages[condition].append(age)

for condition, ages in condition_ages.items():
    avg_age = round(sum(ages) / len(ages), 1)
    print(f"{condition}: {avg_age}")

# Exercise 9: Search by name
print("\n--- Exercise 9: Search for a patient by name ---")
query = input("Enter name to search: ").strip()
found = False
for row in data:
    if query in row['שם']:
        print(row)
        found = True
if not found:
    print("Name not found")

# Exercise 10: Most common first name
print("\n--- Exercise 10: Most common first name ---")
first_names = [row['שם'].split()[0] for row in data if row['שם']]
first_name_counts = Counter(first_names)
most_common = first_name_counts.most_common(1)[0]
print(f"The most common first name is: {most_common[0]} ({most_common[1]} times)")
