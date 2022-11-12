#Is Subsequence
class Solution(object):
    def isSubsequence(self, s: str, t: str):
        count = 0
        for i in s:
            if i in t:
                count += 1

        if count == len(s):
            return True

        else:
            return False

s = Solution()
print(s.isSubsequence("abc", "adbhc"))
print(s.isSubsequence("abc", "adhc"))