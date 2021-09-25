tuple = 1,2,3,4,5
tuple2 = (1,2,3,4,5)
print(type(tuple))
print(type(tuple2))
#a tuple could also include string and booleans
#its also immutable

t = (1)
print(type(t))
#int
t = (1,)
print(type(t))
#tuple

a = [1,2,3]
b = [10,20,30]
t = (*a, *b)
print(t)
#we can unpack items into tuples using * works with all iterable types
#also you cant append a tuple so this is a great way to apend without using apend

car = ('Toyota', 2021, False)
model, year, stolen = car
print(year)
#another way to unpack works with all iterable types