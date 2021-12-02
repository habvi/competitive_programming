# Runtime: 56 ms, faster than 89.91% of Python3 online submissions for Combination Sum.
# Memory Usage: 14.9 MB, less than 6.15% of Python3 online submissions for Combination Sum.

class Solution:
    def combinationSum(self, candidates, target: int):
        n = len(candidates)
        dp = [set() for _ in range(target + 1)]
        dp[0].add((0,))
        for i in range(n):
            for j in range(target):
                if j + candidates[i] <= target:
                    for t in dp[j]:
                        dp[j + candidates[i]].add(t + (candidates[i],))
        ans = []
        for a in dp[target]:
            ans.append(list(a[1:]))
        return ans

# S = Solution()
# a = [2, 3, 5]
# n = 8
# S.combinationSum(a, n)