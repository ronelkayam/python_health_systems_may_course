"""
5.	כתוב פונקציה שמקבלת ערך של המוגלובין ומין המטופל
, ומחזירה אם הערך נמוך/תקין/גבוה.
"""


def get_patient_name():
    return input("please enter your name")


def get_moglobin():
    return int(input(f"hello, please enter your moglobin value:"))


def get_gender_from_patient(name):
    return input(f"hello {name}, enter your gender?m/f only please")


def gender_validation(gender):
    return gender.lower() == "f" or gender.lower() == "m"


def return_male_or_female_by_gender(gender):
    if gender_validation(gender):
        if gender.lower() == "m":
            return "male"
        else:
            return "female"
    else:
        return "error value!"


def get_moglobin_diagnosis_by_male(moglobin_value):
    if moglobin_value < 13:
        return "low, go to doctor"
    elif 13 < moglobin_value <= 17.5:
        return "normal"
    else:
        return "higher"


def get_moglobin_diagnosis_by_female(moglobin_value):
    if moglobin_value < 16:
        return "low, go to doctor"
    elif 16 < moglobin_value <= 20:
        return "normal"
    else:
        return "higher"


def get_normal_moglobin_value_by_gender_and_value(gender):
    moglobin_value = get_moglobin()
    if return_male_or_female_by_gender(gender) == "male":
        if moglobin_value < 13:
            return "low, go to doctor"
        elif 13 < moglobin_value <= 17.5:
            return "normal"
        else:
            return "higher"
    elif return_male_or_female_by_gender(gender) == "female":
        if moglobin_value < 16:
            return "low, go to doctor"
        elif 16 < moglobin_value <= 20:
            return "normal"
        else:
            return "higher"


def first_option():
    print("**********first option*******")
    name = get_patient_name()
    moglobin_value = get_moglobin()
    gender = get_gender_from_patient(name)
    if gender_validation(gender):
        male_or_female = return_male_or_female_by_gender(gender)
        if male_or_female == "male":
            get_moglobin_diagnosis_by_male(moglobin_value)
        else:
            get_moglobin_diagnosis_by_female(moglobin_value)


def second_option():
    print("*******second option*******")
    name = get_patient_name()
    gender = get_gender_from_patient(name)
    if gender_validation(gender):
        male_or_female = return_male_or_female_by_gender(gender)
        get_normal_moglobin_value_by_gender_and_value(male_or_female)


first_option()
second_option()
