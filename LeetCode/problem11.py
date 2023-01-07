#2sum
def TwoSum(nums: list, target: int):
    numsy = nums.copy()
    numsy.remove(nums[0])
    Snum = 0

    for x in nums:
        for y in numsy:
            Snum = x+y
            if Snum == target:
                return f"({nums.index(x)},{numsy.index(y)+1})"
    

print(TwoSum(nums = [2,7,11,15], target = 17))