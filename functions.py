# get and return function
def get_and_return(name):
    print("hello from getAndReturn func")
    return "hello " + name


print(f"out of function\n{get_and_return('Ron')}")


# returnAndNotGet
def return_and_not_get():
    print("hello from returnAndNotGet func")
    return "return from returnAndNotGet func"


return_from_func = return_and_not_get()
print(return_from_func)


# getAndNotReturn func

def get_and_not_return_func(name_for_func):
    print("hello from getAndNotReturn func")


name_from_main = input("please enter your name")
get_and_not_return_func(name_from_main)


# notGetAndNotReturn
def not_get_and_not_return_func():
    print("hello from notGetAndNotReturn func")


not_get_and_not_return_func()
