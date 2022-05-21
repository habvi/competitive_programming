# Runtime: 81 ms, faster than 62.88% of Python3 online submissions for Minimum Size Subarray Sum.
# Memory Usage: 16.9 MB, less than 5.04% of Python3 online submissions for Minimum Size Subarray Sum.

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        from itertools import accumulate
        from bisect import bisect_left

        n = len(nums)

        ac = [0, *accumulate(nums)]
        ans = float('inf')
        for i, a in enumerate(ac):
            bi = bisect_left(ac, a + target)
            if bi == n + 1 and ac[-1] - a < target:
                break
            ans = min(ans, bi - i)

        return ans if ans != float('inf') else 0


# S = Solution()
# target = 7
# nums = [2, 3, 1, 2, 4, 3]
# print(S.minSubArrayLen(target, nums))