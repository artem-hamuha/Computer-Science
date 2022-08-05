def remove_even(nums: list[int]):
    new_nums = []
    for i in nums:
        if i % 2 != 0:
            new_nums.append(i)

    print(new_nums)

remove_even([7, 8, 120, 25, 44, 20, 27])