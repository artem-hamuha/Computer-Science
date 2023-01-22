# String to Integer atoi
class Solution(object):
    def myAtoi(self, s: str):
        MAX_NUM = 2 ** 31 - 1
        MIN_NUM = -2 ** 31
        
        s = s.strip()
        sign = 1
        index = 0
        num = 0
        if not s:
            return num
        
        if s[0] == '-':
            sign = -1
            index += 1
        
        while index < len(s) and s[index].isdigit():
            curr_digit = ord(s[index]) - ord('0')
            if num > MAX_NUM // 10 or (num == MAX_NUM // 10 and curr_digit > 7): # here we do the check before adding current digit
                return MAX_NUM if sign == 1 else MIN_NUM
            num = num * 10 + curr_digit
            index += 1
        
        num = sign * num
        return num    



ans = Solution()
print(ans.myAtoi("4193 with words"))