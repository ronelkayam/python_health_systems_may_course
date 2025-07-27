num_of_medications_in_stock = 4
while num_of_medications_in_stock > 0:
    name = input("please enter your name:")
    temp = int(input("please enter your temp body:"))
    if 36 < temp < 38:
        print(f"{name}, take twice a day after meals!")
        num_of_medications_in_stock -= 1
    else:
        print("I wouldn't recommend taking it to someone with high body temp!")
    print(f"Medications in stock :{num_of_medications_in_stock}")
print("make happen any way!")
