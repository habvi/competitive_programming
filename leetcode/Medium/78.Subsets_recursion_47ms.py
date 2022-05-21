# Runtime: 47 ms, faster than 16.92%
# Memory Usage: 14.5 MB, less than 52.74%

class Solution:
    def subsets(self, nums):
        def dfs(lis, i):
            ans.append(lis)
            for j in range(i + 1, n):
                dfs(lis + [nums[j]], j)

        n = len(nums)
        ans = []
        dfs([], -1)
        return ans

S = Solution()
nums = [1, 2, 3]
# nums = [0]
print(S.subsets(nums))