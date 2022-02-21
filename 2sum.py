nums = [0, 5, 6, 15, 3, 8]
target = 18

def two_sum(list, target):
    prevMap = {}

    for i, n in enumerate(list):
        diff = target - n
        if diff in prevMap:
            return prevMap[diff], i
        prevMap[n] = i

two_sum(nums, target)