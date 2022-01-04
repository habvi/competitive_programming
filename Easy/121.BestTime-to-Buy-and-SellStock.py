# Runtime: 1224 ms, faster than 20.38% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.2 MB, less than 11.34% of Python3 online submissions for Best Time to Buy and Sell Stock.

class Solution:
    def maxProfit(self, prices) -> int:
        hi = prices[-1]
        ans = 0
        for p in reversed(prices[:-1]):
            if p < hi:
                ans = max(ans, hi - p)
            hi = max(hi, p)
        return ans      
        
S = Solution()
p = [7, 1, 5, 3, 6, 4]
# p = [7, 6, 4, 3, 1]
print(S.maxProfit(p))