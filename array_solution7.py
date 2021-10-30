class Solution:
    def plusOne(digits: list[int]):
        # convert list of ints to list of str
        digits = [str(x) for x in digits]
        # join list, conv to int and + 1
        plus_1 = int("".join(digits)) + 1
        # convert back to list of ints
        digits_plus_1 = [int(x) for x in str(plus_1)]
        
        return digits_plus_1

print(Solution.plusOne([1,2,4,0]))