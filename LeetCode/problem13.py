#Median of 2 sorted arrays
def median2arrays(nums1: list[int], nums2: list[int]):
    nums1.extend(nums2)
    nums1.sort()

    if len(nums1)%2==0:
        a=len(nums1)/2
        return float(nums1[a]+nums1[a-1])/float(2)
        
    else:
        a=len(nums1)/2
        return float(nums1[a])