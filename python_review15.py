#list comprehension
l = [x for x in range(0,10)]
print(l)
#example

l = [x for x in range(0,10) if x % 2 > 0]
print(l)
#returns odds

l = [x + 4 for x in [2,4,6]]
print(l)
#adds 4

m = [[j for j in range(3)] for i in range(4)]
print(m)
#nested list comprehension