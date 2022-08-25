def remove_dup(nums: list):
    nums = set(nums)
    nums = list(nums)
    k = len(nums)

    print(k, nums)

remove_dup([1,1,2])