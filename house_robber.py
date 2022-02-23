from operator import index


def house_robber(nums):
    if len(nums)<=2: return max(nums)
    robbing=[nums[0],max(nums[0],nums[1])]
    for i in range(2,len(nums)):
        robbing.append(max(nums[i]+robbing[-2],robbing[-1]))
    return robbing[-1]
        

    

print(house_robber([1, 1, 3, 1]))