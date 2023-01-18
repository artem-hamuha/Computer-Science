#Reverse Int
class Solution(object):
    def reverse(self, x):
        max1 = 2**31 - 1
        min1 = -2**31
        x1 = 1

        if x < 0:
            x1 *= -1
            x *= -1

        final_x = str(x)[::-1]

        final_x = int(final_x) * x1
        
        if final_x >= min1 and final_x <= max1:
            return final_x

        else:
            return 0
                

answ = Solution()
print(answ.reverse(-123))