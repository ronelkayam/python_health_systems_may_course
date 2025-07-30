# declaration
ls = [1, 2, 3, "moshe"]
ls1 = [111, 32, 3, 4]
ls2 = []
ls3 = ["moshe", "david", "ron"]

# print all list
print(ls)  # with [] and ,
for i in ls:
    print(i, end=",")

# print argument
print(f"\nlocation:0  value: {ls1[0]}")
# print(ls[small then list length])

# add argument to list
print(f"\nbefore append: {ls}")
ls.append("new argument")
print(f"after appending: {ls}")

# add in special location-> insert(location,value)
print(f"\nbefore insert: {ls}")
location_to_add = 1
if len(ls) > location_to_add:
    ls.insert(1, "dudu")
print(f"after insert: {ls}")

# delete argument ->argument exists in list
print(f"\nbefore delete: {ls}")
del ls[0]
print(f"after delete: {ls}")

# list length
print(f"ls length: {len(ls)}")

# sort list
# 1 option
sortList = sorted(ls1)
print("** sorted function***")
print(f"unsorted list :{ls1}")
print(f"sorted list: {sortList}")

# option 2
print("***sort function****")
lss = [143, 23, 55, 6]
print(f"unsorted list :{lss}")
lss.sort()
print(f"sorted list: {lss}")