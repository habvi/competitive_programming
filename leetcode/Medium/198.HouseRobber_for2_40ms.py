# Runtime: 40 ms, faster than 39.53% of Python3 online submissions for House Robber.
# Memory Usage: 13.9 MB, less than 95.94% of Python3 online submissions for House Robber.

class Solution:
    def rob(self, nums) -> int:
        n = len(nums)

        dp = [0] * n
        dp[:2] = nums[:2]
        for i in range(n):
            for j in range(i - 1):
                dp[i] = max(dp[i], dp[j] + nums[i])
                
        return max(dp)


# S = Solution()
# nums = [2,1,1,2]
# nums = [2,1,1,2,4,1,6]
# nums = [1,2,3,1]
# nums = [2,7,9,3,1]
# nums = [2]
# print(S.rob(nums))
