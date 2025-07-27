"""
This is a function tutorial with 4 functions kinds
"""


def get_and_return_func(name, last_name):
    print("hello from get_and_return_func")
    return f"hello {name}"


new_name = get_and_return_func("ron", "Elkayam")
print(f"out from get_and_return_func, return value: {new_name}")
print("*********************************")


def not_get_and_not_return_func():
    print("hello from not_get_and_not_return_func")


not_get_and_not_return_func()
print("printing out of not_get_and_not_return_func")
print("***********************")


def get_and_not_return_func(name, temp_body):
    print("hello from get_and_not_return_func")
    if temp_body > 38:
        print(f"{name} go argent to doctor and take optalgin!")
    else:
        print(f"{name} you are healthy, go home and drink tea:)")


def enter_name():
    return input("please enter your name")


def enter_temp_body():
    return float(input("please enter temp body:"))


f_name = enter_name()
temp = enter_temp_body()

get_and_not_return_func(f_name, temp)
f_name = enter_name()
temp = enter_temp_body()
get_and_not_return_func(f_name, temp)


def return_and_not_get_func():
    return "good bye, vahe a nice day:)"


ret = return_and_not_get_func()
print(ret)

print(return_and_not_get_func())
