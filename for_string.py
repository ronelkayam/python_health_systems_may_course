DNA = input("please enter your DNA:")
print(f"Your DNA :{DNA}")
t_count = 0
for char in DNA:
    if char == "t" or char == "T":
        t_count += 1
print(f"num of t appears in DNA is:{t_count} ")
