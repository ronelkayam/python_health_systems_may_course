beds_num = 20
while beds_num > 0:
    there_is_place = input("there is a free beds to patients?")
    if there_is_place == "no":
        continue
    temp = int(input("please enter your temp body:"))
    if temp > 38:
        print("you are sick, being to hospitalized")
        beds_num -= 1
    else:
        print("you are healthy, go home!")
print(beds_num)

