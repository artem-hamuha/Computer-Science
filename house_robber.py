#my code
def house_robber(nums):
    max_num = max(nums)
    if nums.index(max_num) == 0:
        right = nums[nums.index(max_num) + 1]
        nums.remove(right)
        nums.remove(max_num)
        max_num2 = max(nums)
        return max_num + max_num2
    elif nums.index(max_num) == len(nums) - 1:
        left = nums[nums.index(max_num) - 1]
        nums.remove(left)
        nums.remove(max_num)
        max_num2 = max(nums)
        return max_num + max_num2
    else:
        left = nums[nums.index(max_num) - 1]
        right = nums[nums.index(max_num) + 1]
        nums.remove(left)
        nums.remove(right)
        nums.remove(max_num)
        max_num2 = max(nums)
        return max_num + max_num2

print(house_robber([1, 2, 9, 4, 5, 0, 8]))