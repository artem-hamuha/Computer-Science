class Solution:
    def twoSum(nums: list[int], target: int):
        for i,val in enumerate(nums):
            first_index = i
            sec_num = target - val
            if sec_num in nums[i+1:] :
                return first_index,nums.index(sec_num,i+1)

print(Solution.twoSum([1,2,3,4,5,6,7,8,9,10], 15))