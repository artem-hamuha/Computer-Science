#Running Sum of 1d Array
class Solution(object):
    def runningSum(self, nums:list[int]):
        lst = []
        num = 1

        while len(lst) != len(nums):
            lst.append(sum((nums[0:num])))
            num += 1

        print(lst)

S = Solution()
S.runningSum([1,2,3,4])