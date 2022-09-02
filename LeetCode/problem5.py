def singleNum(nums: list[int]):
    n=len(nums)
    r=nums[0]
    for i in range(1,n):
        r = r ^ nums[i] 

    return r

singleNum([1,4,2,1,2])