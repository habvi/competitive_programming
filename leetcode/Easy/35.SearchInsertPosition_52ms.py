# Runtime: 52 ms, faster than 56.61% of Python3 online submissions for Search Insert Position.
# Memory Usage: 15.1 MB, less than 24.37% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        from bisect import bisect
        bi = bisect(nums, target)
        if bi == 0:
            return 0
        if nums[bi - 1] == target:
            return bi - 1
        else:
            return bi