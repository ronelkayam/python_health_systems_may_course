count = 0
for i in range(20):
    if i % 3 == 0:
        print(f"{i}, divide by 3 without rest, continue")
        continue
    print(i)
    count += 1
    print(f"count:{count}")
