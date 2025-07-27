num_of_medications_in_stock = 10
for medication in range(1, num_of_medications_in_stock + 1):
    name = input("please enter your name:")
    print(f"{name}, take twice a day after meals!")
    print(f"Medications in stock :{num_of_medications_in_stock - medication}")
print("make happen any way!")
