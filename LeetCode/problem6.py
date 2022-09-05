import collections

def intersect(nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    print(list((a & b).elements()))

intersect(nums1 = [1,2,2,1], nums2 = [2,2])
intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])