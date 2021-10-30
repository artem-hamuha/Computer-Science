class Solution:
    def moveZeroes(nums: list[int]):
        for i in nums:
            if(i==0):
                nums.remove(i)
                nums.insert(len(nums),0)
        return nums

print(Solution.moveZeroes([0,0,0,0,2,0,99,20]))