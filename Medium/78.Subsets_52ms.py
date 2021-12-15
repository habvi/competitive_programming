# Runtime: 39 ms, faster than 25.78%
# Memory Usage: 14.5 MB, less than 52.74%

class Solution:
    def subsets(self, nums):
        n = len(nums)
        ans = []
        for i in range(1 << n):
            ans.append([nums[j] for j in range(n) if i&(1 << j)])
        return ans

S = Solution()
nums = [1, 2, 3]
# nums = [0]
print(S.subsets(nums))