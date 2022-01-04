# Runtime: 64 ms, faster than 47.32% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 15 MB, less than 89.66% of Python3 online submissions for Best Time to Buy and Sell Stock II.

class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        for i in range(len(prices) - 1):
            p1, p2 = prices[i], prices[i + 1]
            if p1 < p2:
                ans += p2 - p1
        return ans
        
S = Solution()
p = [7, 1, 5, 3, 6, 4]
# p = [1, 2, 3, 4, 5]
# p = [7, 6, 4, 3, 1]
print(S.maxProfit(p))