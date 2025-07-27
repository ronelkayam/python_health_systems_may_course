import csv


def read_ages_patients_from_csv(file_name):
    patients = []
    with open(file_name, newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row['גיל'] = int(row['גיל'])
            patients.append(row)
    return patients

def read_medical_status_from_csv(file_name):
    patients = []
    with open(file_name, newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row['מצב רפואי'] = row['מצב רפואי']
            patients.append(row)
    return patients


def filter_patients_over_40(patients):
    # patients_over_40=[]
    # for patient in patients:
    #     if patient['גיל']>40:
    #         patients_over_40.append(patient)
    # return patients_over_40
    return [patient for patient in patients if patient['גיל'] > 40]


def write_patients_to_csv(file_name, patients):
    if not patients:
        print("no data to save!")
        return
    header = ['שם', 'גיל', 'מצב רפואי']
    print(patients)
    with open(file_name, 'w', encoding='utf-8') as new_file:
        writer = csv.DictWriter(new_file, fieldnames=header)
        writer.writeheader()
        writer.writerows(patients)

def filter_healthy_patients(patients_over_40):
    return [patient for patient in patients_over_40 if patient['מצב רפואי'] !='בריא']




source_file = 'patients.csv'
over_40_file = 'patients_over_40.csv'
healthy_and_over_40_file = "patients_healthy_over_40.csv"
all_patients = read_ages_patients_from_csv(source_file)
patients_over_40 = filter_patients_over_40(all_patients)
write_patients_to_csv(over_40_file, filter_patients_over_40)
print(f"{len(patients_over_40)} patients are saved in {over_40_file}")
medical_status_over_40_patients = read_medical_status_from_csv(over_40_file)
healthy_and_over_40 = filter_healthy_patients(medical_status_over_40_patients)
print(f"{len(healthy_and_over_40)} patients are saved in {healthy_and_over_40_file}")
