from random import shuffle


def shuffle_list(nums: list[int]):
    shuffle(nums)
    print(nums)
shuffle_list([1,2,3,4,5])