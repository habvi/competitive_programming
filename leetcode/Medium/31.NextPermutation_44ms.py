# 44ms, 60.16%
# 14.1MB, 81.27%

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from bisect import bisect
        n = len(nums)
        increase = []
        after = []
        pre = 0
        for i in range(n - 1, -1, -1):
            if nums[i] >= pre:
                increase.append(nums[i])
                pre = nums[i]
                continue
            else:
                bi = bisect(increase, nums[i])
                nums[i], increase[bi] = increase[bi], nums[i]
                after = nums[:i + 1] + increase
                break
        else:
            after = nums[::-1]

        for i in range(n):
            nums[i] = after[i]

# S = Solution()
# nums = [1, 3, 2]
# nums = [1, 1, 5]
# nums = [2, 1, 3]
# nums = [1, 2, 3]
# nums = [2, 3, 1, 3, 3]
# nums = [4, 5, 1, 3, 2]
# nums = [2, 2, 7, 5, 4, 3, 2, 2, 1]
# nums = [3, 2, 1]
# S.nextPermutation(nums)
# print(nums)