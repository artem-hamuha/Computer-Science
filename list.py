aList = [100, 200, 300, 400, 500]
aList = aList[::-1]

print(aList)

list1 = ["M", "na", "i", "Ar"] 
list2 = ["y", "me", "s", "tem"]
list3 = [i + j for i, j in zip(list1, list2)]

print(*list3, sep=" ")