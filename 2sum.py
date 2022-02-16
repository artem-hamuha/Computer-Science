nums = [0, 5, 6, 15, 3, 8]
target = 18

for i in range(len(nums)):
    dl = nums
    diff = target - nums[i]
    dl[i]=None
    if(diff in dl):
        res = []
        res.extend([i,dl.index(diff)])
        print(res)