# Runtime: 915 ms, faster than 5.02%
# Memory Usage: 55.6 MB, less than 9.42%

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = float('inf')
    def minDepth(self, root, depth=1) -> int:
        if not root:
            return 0

        if root.left:
            self.ans = min(self.ans, self.minDepth(root.left, depth + 1))
        if root.right:
            self.ans = min(self.ans, self.minDepth(root.right, depth + 1))
            
        if not root.left and not root.right:
            return depth
        return self.ans