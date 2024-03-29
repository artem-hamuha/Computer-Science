#Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        ans = ""
        for i in range(n):
            dp[i][i] = 1
            ans = s[i]
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1]=1
                ans = s[i:i+2]
                
        for j in range(1, n):
            for i in range(0, j-1):
                if dp[i+1][j-1] ==1 and s[i]==s[j]:
                    dp[i][j] = 1
                    if len(ans) < j-i+1:
                        ans = s[i:j+1]
        return ans

asw = Solution()
print(asw.longestPalindrome(s = "babad"))