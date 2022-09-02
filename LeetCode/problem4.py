def containsDup(nums: list[int]):
    if set(nums) == nums:
        print(False)
    else:
        print(True)

containsDup([1,2,3,4,5,5,6])