class Solution:
    def maxProfit(prices: list[int]):
        res=0
        for  p in range(len(prices)-1):
            if prices[p]<=prices[p+1]:
                res+=prices[p+1]-prices[p]    
        return res

print(Solution.maxProfit([9,6,8,1,4,5]))