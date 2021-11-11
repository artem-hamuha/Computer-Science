class Solution:
    def mergeLists(l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            l3 = l1 + l2
            return sorted(l3)

print(Solution.mergeLists([1,2,4], [1,3,4]))
print(Solution.mergeLists([],[]))