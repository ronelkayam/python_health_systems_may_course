import csv


def read_patients_from_csv(file_name):
    patients = []
    with open(file_name, newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row['גיל'] = int(row['גיל'])
            patients.append(row)
    return patients


def filter_patients_over_40(patients):
    # patients_over_40=[]
    # for patient in patients:
    #     if patient['גיל']>40:
    #         patients_over_40.append(patient)
    # return patients_over_40
    return [patient for patient in patients if patient['גיל'] > 40 and patient['מצב רפואי'] != 'בריא']


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


input_file = 'patients.csv'
output_file = 'patients_over_40.csv'
all_patients = read_patients_from_csv(input_file)
filter_patients = filter_patients_over_40(all_patients)
write_patients_to_csv(output_file, filter_patients)
print(f"{len(filter_patients)} patients are saved in {output_file}")
