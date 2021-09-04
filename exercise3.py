def even_list(x):
    nums = []
    for n in x:
        if n % 2 == 0:
            nums.append(n)
    return nums
print(even_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def odd_list(x):
    nums = []
    for n in x:
        if n % 2 > 0:
            nums.append(n)
    return nums
print(odd_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))