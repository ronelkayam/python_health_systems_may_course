name = input("please enter your name:")
temp = float(input("please enter temp body:"))
bpm = int(input("please enter your bpm:"))
systolic = int(input("please enter systolic:"))
if temp>37.9:
    print(f"{name}, you have fever")
    if systolic>90:
        if bpm>100:
            print(f"{name}, emergency! possible sepsis")
        else:
            print(f"{name}, your fever and systolic is high, but bpm is normal")
    else:
        print(f"{name}, systolic is normal but fever is fever")
else:
    print(f"{name}, fever is normal, patient seems stable:)")
