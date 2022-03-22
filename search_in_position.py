def search_in_position(nums: list[int], target):
    last = nums[len(nums)-1]

    if last <= target:
        return nums.index(last) + 1

    else:
        for i in nums:
            if i == target:
                return nums.index(target)
            
            elif i > target:
                return nums.index(i)

print(search_in_position([1,3,5,6], 8))