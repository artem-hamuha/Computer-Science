#input array is sorted
def two_sum(nums, target):
    l = len(nums) - 1
    on = True
    while on:
        if nums[l] > target:
            nums.remove(nums[l])
            l -= 1
        else:
            on = False
    
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            print(prevMap[diff], i)
        prevMap[n] = i

two_sum([2,7,11,15], 9)
