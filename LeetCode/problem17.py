#Regular expression matching
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.search("." + p + "*", s)!=None

ans = Solution()
print(ans.isMatch("ab", "c*a*b"))