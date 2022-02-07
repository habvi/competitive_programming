# Runtime: 68 ms, faster than 96.27% of Python3 online submissions for Minimum Size Subarray Sum.
# Memory Usage: 16.7 MB, less than 17.33% of Python3 online submissions for Minimum Size Subarray Sum.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        from collections import deque

        q = deque()
        ans = float('inf')
        total = 0
        for num in nums:
            q.append(num)
            total += num

            while q and total >= target:
                ans = min(ans, len(q))
                rm = q.popleft()
                total -= rm

        return ans if ans != float('inf') else 0


# S = Solution()
# target = 7
# nums = [2,3,1,2,4,3]
# print(S.minSubArrayLen(target, nums))