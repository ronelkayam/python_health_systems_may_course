"""
5.	צור dictionary של רופאים והדפס רק את הרופאים שהם פרופסורים ומעל גילאי 60
"""

doctors = [{
    "name": "mohamad",
    "title": "prof",
    "age": 40,
    "id": 20003332,
    "specialization": "orthopedist",
    "seniority": 15
},
    {
        "name": "dan",
        "age": 65,
        "title": "prof",
        "id": 20987799,
        "specialization": "cancer",
        "seniority": 35
    }
    ,
    {
        "name": "cohen",
        "age": 63,
        "id": 20246675,
        "title": "prof",
        "specialization": "kids",
        "seniority": 25
    }
    , {
        "name": "esham",
        "age": 62,
        "id": 20355332,
        "title": "dr",
        "specialization": "generic",
        "seniority": 7
    }]

for doctor in doctors:
    if doctor.get("title") == "prof" and doctor.get("age") > 60:
        print("**********professor details:***********")
        for key, value in doctor.items():
            print(f"{key}:{value}")
        print("\n\n")

"""
8.	הגדירו את ה dictionary הבא:
patients = [
    {"name": "Dana", "age": 30, "diagnosis": "flu"},
    {"name": "Yossi", "age": 45, "diagnosis": "diabetes"},
    {"name": "Fatima", "age": 28, "diagnosis": "asthma"}
]
הדפיסו את שמות המטופלים עם הגיל לידם
הדפיסו רק את המטופלים שמעל גיל 40
הוסיפו ליד כל מטופל בי"ח שהוא מטופל בו

"""

patients = [
    {"name": "Dana", "age": 30, "diagnosis": "flu"},
    {"name": "Yossi", "age": 45, "diagnosis": "diabetes"},
    {"name": "Fatima", "age": 28, "diagnosis": "asthma"}
]
print("All names&age patients")
for patient in patients:
    print(f"{patient.get('name')},{patient.get('age')} ")

print("\n\nAll over 40 patients details")
for patient in patients:
    if patient.get("age") > 40:
        print(f"{patient.get('name')},{patient.get(('age'))},{patient.get('diagnosis')}")

for patient in patients:
    hospital = input(f"{patient.get('name')} please enter your hospital:")
    patient["hospital"] = hospital
print("\n\nAll patients after adding hospital:\n")
for patient in patients:
    print(f"{patient.get('name')},{patient.get('age')},"
          f"{patient.get('diagnosis')},{patient.get('hospital')}")
