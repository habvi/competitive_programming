# Runtime: 112 ms, faster than 16.88%
# Memory Usage: 15.7 MB, less than 60.82%

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def divide(l, r):
            if l >= r:
                return None
            m = l + (r - l) // 2
            root = TreeNode(nums[m])
            root.left = divide(l, m)
            root.right = divide(m + 1, r)
            return root
        n = len(nums)
        return divide(0, n)