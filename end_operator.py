# end operator example
name = "Ron"
age = 34
city = "Kiryat-gat"
print("without end operator")

print(f"my name {name}")
print(f"my age is {age}")
print(f"i'm living in {city}")

print(f"\n\nwith end seperator")
print(f"my name {name}", end="*end seperator*")
print(f"my age is {age}", end="*end seperator*")
print(f"i'm living in {city}")
