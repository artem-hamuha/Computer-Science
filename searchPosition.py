class Solution:
    def searchInsert(nums: list[int], key: int) -> int:
        
        i, j = 0, len(nums)-1
        
        while i <= j:
            m = (i + j) // 2
            mid = nums[m]
            if mid > key : j = m - 1
            elif mid < key : i = m + 1
            else : return m
        else:
            return i

print(Solution.searchInsert([1,3,5,6], 5))
print(Solution.searchInsert([1,3,5,6], 2))