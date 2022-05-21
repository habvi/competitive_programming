# Runtime: 36 ms, faster than 90.09% of Python3 online submissions for Permutations.
# Memory Usage: 14.5 MB, less than 45.98% of Python3 online submissions for Permutations.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        ans = []
        for per in permutations(nums, len(nums)):
            ans.append(list(per))
        return ans