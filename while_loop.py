num_of_medications_in_stock = 10
while num_of_medications_in_stock > 0:
    name = input("please enter your name:")
    print(f"{name}, take twice a day after meals!")
    num_of_medications_in_stock -= 1
    print(f"Medications in stock :{num_of_medications_in_stock}")
print("make happen any way!")
