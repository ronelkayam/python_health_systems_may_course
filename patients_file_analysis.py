import csv
from collections import defaultdict, Counter
from statistics import mean

# Function to read patient data from a CSV file
def read_patients_csv(filepath):
    patients = []
    with open(filepath, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                name = row['שם'].strip()
                age = int(row['גיל'].strip())
                condition = row['מצב רפואי'].strip()
                patients.append({'name': name, 'age': age, 'condition': condition})
            except (ValueError, KeyError):
                continue
    return patients

patients = read_patients_csv("patients.csv")
