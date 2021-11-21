# Runtime : 68ms, 55.49%
# Memory : 15.8MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ordered_nums = [(num, i) for i, num in enumerate(nums)]
        ordered_nums.sort()

        n = len(nums)
        right_i = n - 1
        for left_i in range(n):
            while True:
                if ordered_nums[right_i][0] <= target - ordered_nums[left_i][0]:
                    break
                right_i -= 1

            if ordered_nums[left_i][0] + ordered_nums[right_i][0] == target:
                return ordered_nums[left_i][1], ordered_nums[right_i][1]