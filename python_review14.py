def f(*, a, b):
    return a, b

print(f(a=1, b=3))
#you can force this print statement brecause of the '*'

def f(a, b):
    return a, b

args = {"a": 1, "b": 2}
print(f(*args))
print(f(**args))

def f(a,b,c):
    return a,b,c

array = [1,2,3]
print(f(*array))
#using '*' and '**' to unpack dictionaries and arrays

def print_argument(func):
    def wrapper(the_number):
        print("Argument for", func.__name__, "is", the_number)
        return func(the_number)
    return wrapper

@print_argument
def add_one(x):
    return x + 1

print(add_one(1))
#decorating functions

add_10 = lambda x: x + 10
print(add_10(20))

nums = (1,2,3,4)
times_2 = map(lambda x: x * 2, nums)
print(list(times_2))
#using lambda and map