# Runtime: 57 ms, faster than 15.53% of Python3 online submissions for Path Sum.
# Memory Usage: 15 MB, less than 77.59% of Python3 online submissions for Path Sum.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = float('inf')
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, total=0) -> bool:
        if not root:
            return False
        
        total += root.val
        if not root.left and not root.right:
            return total == targetSum
        
        if self.hasPathSum(root.left, targetSum, total):
            return True
        if self.hasPathSum(root.right, targetSum, total):
            return True
        return False