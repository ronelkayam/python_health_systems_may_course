students = [
    {
        "name": "ron",
        "age": 34,
        "grades": [100, 34, 76, 89, 90]
    },
    {
        "name": "david",
        "age": 30,
        "grades": [100, 34, 55, 90, 90]
    }
]

avg = 0
for student in students:
    sum=0
    for grade in student.get("grades"):
        sum += grade
    if sum / len(student["grades"]) > avg:
        avg = sum / grade

