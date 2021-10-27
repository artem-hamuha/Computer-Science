class Solution(object):
    def singleNumber(nums):
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()

print(Solution.singleNumber([1,1,2,2,3,3,4,4,5,6,6]))