class Solution:
    def isPalindrome(x):
        if x<0:
            return False
    
        if x==0:
            return True
    
        num_str=str(x)
    
        nsr=num_str[::-1]
    
        if num_str==nsr:
            return True
    
        else:
            return False

print(Solution.isPalindrome(6))

num = '1234567890'
print(num[::-1])