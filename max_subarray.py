def max_subarray(nums):
    max_sum = 0
    cur_sum = 0
    for n in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += n
        if max_sum < cur_sum:
            max_sum = cur_sum
    print(max_sum)

max_subarray([-2,1,-3,4,-1,2,1,-5,4])