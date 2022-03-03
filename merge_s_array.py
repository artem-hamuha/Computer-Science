# the answear must be in num1(put num2 in num1)
def merge_sorted_array(num1: list[int], m: int, num2: list[int], n: int):
    while n != -1:
        num1[m] = num2[n]
        m -= 1
        n -= 1
    return sorted(num1)



print(merge_sorted_array([1,2,3,0,0,0], 5, [2,5,6], 2))