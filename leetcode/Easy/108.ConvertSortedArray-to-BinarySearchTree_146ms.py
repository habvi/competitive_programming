# Runtime: 146 ms, faster than 5.15%
# Memory Usage: 15.7 MB, less than 16.98%

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        n = len(nums) // 2
        root = TreeNode(nums[n])
        root.left = self.sortedArrayToBST(nums[:n])
        root.right = self.sortedArrayToBST(nums[n + 1:])
        return root