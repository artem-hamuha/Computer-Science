class Solution:
    def intersect(nums1: list[int], nums2: list[int]):
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        
        arr = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                arr.append(nums1[i])
                i += 1
                j += 1
                
            elif nums1[i] < nums2[j]:
                i += 1
                
            elif nums1[i] > nums2[j]:
                j += 1
                
        return arr

print(Solution.intersect([1,2,3,4,5,6],[9,8,7,6,5]))