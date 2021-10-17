def removeDuplicates(nums: list[int]):
        nextP = 0
        for i in range (0, len(nums)):
            if nums[i] != nums[nextP]:
                nextP += 1
                nums[nextP] = nums[i]     
        return nextP + 1

