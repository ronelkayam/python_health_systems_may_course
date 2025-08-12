"""
string_formatting_explained.py

This file explains how the format() method works in Python for string formatting.
"""

# Basic usage
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Alice and I am 30 years old.

# Using positional arguments
print("Hello {0}, you are {1} years old. Yes, {0}, it's true.".format(name, age))
# Output: Hello Alice, you are 30 years old. Yes, Alice, it's true.

# Using keyword arguments
print("Hello {first}, you are {second} years old.".format(first=name, second=age))
# Output: Hello Alice, you are 30 years old.

# Formatting numbers
pi = 3.14159265
print("Pi rounded to 2 decimal places: {:.2f}".format(pi))
# Output: Pi rounded to 2 decimal places: 3.14

# Padding and alignment
text = "Hello"
print("|{:<10}|{:^10}|{:>10}|".format(text, text, text))
# Output: |Hello     |  Hello   |     Hello|

# Padding with custom characters
print("|{:_<10}|{:*^10}|{:->10}|".format(text, text, text))
# Output: |Hello_____|**Hello***|-----Hello|

# Formatting integers in different bases
number = 255
print("Decimal: {0:d}, Hex: {0:x}, Octal: {0:o}, Binary: {0:b}".format(number))
# Output: Decimal: 255, Hex: ff, Octal: 377, Binary: 11111111

# Using format() with dictionaries
person = {'name': 'Bob', 'age': 25}
print("Name: {p[name]}, Age: {p[age]}".format(p=person))
# Output: Name: Bob, Age: 25

# Nested formatting
template = "The value is {:0{width}d}"
print(template.format(42, width=5))
# Output: The value is 00042

# Mixing types
print("Name: {}, Age: {}, Pi: {:.2f}".format("Charlie", 40, 3.14159))
# Output: Name: Charlie, Age: 40, Pi: 3.14

"""
Summary:
- {} is a placeholder in the string.
- You can use positional or keyword arguments inside {}.
- You can format numbers, control alignment, width, and padding.
- format() is a powerful way to build strings cleanly.
"""

