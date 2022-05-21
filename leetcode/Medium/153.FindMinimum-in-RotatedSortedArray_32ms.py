# Runtime: 32 ms, faster than 98.31% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14.4 MB, less than 91.38% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

class Solution:
    def findMin(self, nums) -> int:
        n = len(nums)
        
        def divide_and_rule(left, right):
            if right - left == 1:
                return nums[left]
            
            mid = (left + right) // 2
            return min(divide_and_rule(left, mid), divide_and_rule(mid, right))
        
        return divide_and_rule(0, n)


# S = Solution()
# nums = [4,5,6,7,0,1,2]
# nums = [3,4,5,1,2]
# nums = [2, 1]
# print(S.findMin(nums))