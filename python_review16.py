iterable = range(0,2)
iterator = iterable.__iter__()

print(iterator.__next__())
print(iterator.__next__())
#iterator and iterables

iterator = range(0,2).__iter__()

print(iterator.__next__())
print(iterator.__next__())
#2 in one

mystring = "ABC"
for letter in mystring:
    print(letter)

mylist = ['A', 'B', 'C']
for letter in mylist:
    print(letter)
#iterator in for loop

print([x for x in 'ABC'])
print([x for x in [1,2,3,4] if x > 2])
#iterators in comprehensions

d = {'name': 'Anna', 'age': 23, 'country': 'Norway' }

for x,y in d.items():
    print(x,y)

print([(x,y) for x, y in d.items()])

#iterating dictionary

with open('python_review15.py') as python_review15:
    for line in python_review15:
        print(line)
#loop over file

class My_Iterator:
    last = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        self.last += 2
        if self.last > 10:
            raise StopIteration
        return self.last

num = My_Iterator()

for x in num:
    print(x)