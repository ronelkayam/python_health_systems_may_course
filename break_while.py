count = 0
i = 1
while count < 20:
    if i % 3 == 0:
        print(f"{i}, divide by 3 without rest, break")
        break
    print(i)
    i += 1
    count += 1
    print(f"count:{count}")
print("out of loop:)")
