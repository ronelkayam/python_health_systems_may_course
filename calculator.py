def plus(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multi(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num1 == 0:
        return -1
    else:
        num1 / num2
        return None


def divide_no_modulo(num1, num2):
    if num1 == 0:
        return -1
    else:
        num1 // num2
        return None


# print(plus(4, 45))
print("welcome to our calculator:\n\n")
num1 = int(input("please enter first number:"))
sign = input("please enter sign: ")
num2 = int(input("please enter second number: "))
if sign == '+':
    print(plus(num1, num2))
elif sign == '-':
    print(minus(num1, num2))
elif sign == '*':
    print(multi(num1, num2))
elif sign == '/':
    print(divide(num1, num2))
elif sign == '//':
    print(divide_no_modulo(num1, num2))
else:
    print("wrong sign choice!!!")
