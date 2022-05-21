# Runtime: 44 ms, faster than 92.93% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.9 MB, less than 82.30% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        return bisect_left(nums, target)