i = 7761060650761587516010615065
print(i)
#you can create a very large integer(even larger than my variable i)

print(int('100'))
print(str(100))
print(int(100.6591))
#converting to diffrent data types

import random

print(random.randint(0, 10))
#random integer using random moduel

print(type(2))
#normal type returns int

if isinstance(2, int):
    print('this is an integer')

#this is basicly using type in a if statement
#its much better than using: if type(2) == int