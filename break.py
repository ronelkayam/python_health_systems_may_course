beds_num = 20
while beds_num > 0:
    temp = int(input("please enter your temp body:"))
    if temp > 38:
        print("you are sick, being to hospitalized")
        beds_num -= 1
    there_is_place = input("there is a free beds to patients?")
    if there_is_place == "no":
        break
    print("bkla blka")
    print("bkla blka")
    print("bkla blka")
    print("bkla blka")
    print("bkla blka")

print(beds_num)
