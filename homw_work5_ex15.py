"""
15.	כתוב פונקציה שמקבלת רשימה של שמות חולים
 ומחזירה רשימה חדשה שבה כל שם מוצג באותיות גדולות (UPPER CASE).
"""


def get_patient_name():
    return input("patient name:")


def create_patients_list():
    ls = []
    size = int(input("please enter size required:"))
    for patient in range(0, size):
        ls.append(get_patient_name())
    return ls

def return_ls_upper(ls):
    upper_ls = []
    for patient in ls:
        upper_ls.append(patient.upper())
    return upper_ls

ls = create_patients_list()
upper_ls = return_ls_upper(ls)