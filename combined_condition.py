name = input("please enter your name:")
temp = float(input("please enter temp body:"))
systolic = int(input("please enter systolic:"))
diastolic = int(input("please enter diastolic:"))
bpm = int(input("please enter bpm:"))
if  temp>38 and bpm>100:
    print(f"{name}, go to doctor right now!")
if systolic>120 or diastolic>80:
    print(f"{name}, take short rest please")
print("make happen any way")