class Solution:
    def mergeLists(l1: list[int], l2: list[int]):
        l3 = l1 + l2
        return sorted(l3)

print(Solution.mergeLists([1,2,4], [1,3,4]))