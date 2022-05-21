# Runtime: 44 ms, faster than 50.32%
# Memory Usage: 16.7 MB, less than 9.44%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.depth = 0
    
    def maxDepth(self, root: Optional[TreeNode], d=0) -> int:
        if not root:
            return d
        self.depth = max(self.depth, self.maxDepth(root.left, d + 1))
        self.depth = max(self.depth, self.maxDepth(root.right, d + 1))
        return self.depth