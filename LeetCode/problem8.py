#Find Pivot Index
class Solution(object):
    def pivotIndex(self, nums: list[int]):
        total=sum(nums)
        leftSum=0

        for i in range(len(nums)):
            total-=nums[i]

            if total==leftSum:
                return i
 
            leftSum+=nums[i]

        return -1

s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))
