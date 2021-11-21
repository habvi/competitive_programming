'''
Runtime : 101ms, 44.55%
Memory : 15.9MB
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from bisect import bisect, bisect_left

        plus = abs(min(nums))
        target += plus * 2
        ordered_nums = [(num + plus, i) for i, num in enumerate(nums)]
        ordered_nums.sort()
        MIN = 0
        MAX = 10**4 + 5

        target_i = bisect(ordered_nums, (target, MAX))
        for right in range(target_i - 1, 0, -1):
            right_num, right_i = ordered_nums[right]
            
            left = bisect_left(ordered_nums, (target - right_num, MIN))
            left_num, left_i = ordered_nums[left]

            if left_num + right_num == target:
                return left_i, right_i