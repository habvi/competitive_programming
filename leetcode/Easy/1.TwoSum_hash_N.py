# Runtime : 55ms, 90.41%
# Memory : 15.3MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elems = {}
        for i, num in enumerate(nums):
            find_num = target - num
            if find_num in elems:
                return elems[find_num], i
            elems[num] = i