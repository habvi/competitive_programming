# Runtime: 736 ms, faster than 73.00% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 28.5 MB, less than 71.52% of Python3 online submissions for Maximum Subarray.

class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        pre = nums[0]
        ans = nums[0]
        for i in range(1, n):
            pre += nums[i]
            if pre < nums[i]:
                pre = nums[i] 
            ans = max(ans, pre)
        return ans

# S = Solution()
# nums = [-2,1,-3,4,-1,2,1,-5,4]   # 6
# nums = [-1]      # -1
# nums = [-2, -1]  # -1
# nums = [-1, 0]   # 0
# print(S.maxSubArray(nums))