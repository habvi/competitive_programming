# Runtime: 112 ms, faster than 16.88%
# Memory Usage: 15.7 MB, less than 60.82%

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def half(l, r):
            if l >= r:
                return None
            m = l + (r - l) // 2
            root = TreeNode(nums[m])
            root.left = half(l, m)
            root.right = half(m + 1, r)
            return root
        n = len(nums)
        return half(0, n)