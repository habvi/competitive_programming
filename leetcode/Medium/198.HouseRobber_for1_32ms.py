# Runtime: 32 ms, faster than 75.73% of Python3 online submissions for House Robber.
# Memory Usage: 13.9 MB, less than 98.82% of Python3 online submissions for House Robber.

class Solution:
    def rob(self, nums) -> int:
        n = len(nums)

        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        
        return max(dp), dp[-1]


# S = Solution()
# nums = [2,1,1,2]
# nums = [2,1,1,2,4,1,6]
# nums = [1,2,3,1]
# nums = [2,7,9,3,1]
# nums = [2]
# print(S.rob(nums))