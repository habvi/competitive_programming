# Runtime: 672 ms, faster than 95.51% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 28.6 MB, less than 59.26% of Python3 online submissions for Maximum Subarray.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        pre = nums[0]
        ans = nums[0]
        for i in range(1, n):
            pre += nums[i]
            if pre < nums[i]:
                pre = nums[i] 
            if ans < pre:
                ans = pre
        return ans