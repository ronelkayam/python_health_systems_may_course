with open('patients.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

header = lines[0].strip().split(',')
names_ls=[]
for line in lines[1:]:  # דילוג על כותרת
    values = line.strip().split(',')

    name = values[0]
    age = int(values[1])
    condition = values[2]

    names_ls.append(values[0])

    print(f":שם{name}, גיל: {age}, מצב: {condition}")

    if age > 40:
        print(f"{name} צריך בדיקה תקופתית")



# כתיבת קובץ חדש עם שמירת נתונים חדשה
with open('over_40.csv', 'w', encoding='utf-8') as out_file:
    out_file.write(','.join(header) + '\n')  # כותב כותרת

    for line in lines[1:]:
        values = line.strip().split(',')
        age = int(values[1])

        if age > 40:
            out_file.write(line)
