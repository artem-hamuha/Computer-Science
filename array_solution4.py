class Solution:
    def ContainsDuplicate(my_list: list):
        my_len = my_list.__len__()
        my_set = set(my_list)
        set_len = my_set.__len__()
        if my_len > set_len:
            return False
        else:
            return True

print(Solution.ContainsDuplicate([1,2,3,4]))
print(Solution.ContainsDuplicate([1,1,2,3]))