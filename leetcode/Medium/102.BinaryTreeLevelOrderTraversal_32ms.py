# Runtime: 32 ms, faster than 84.49%
# Memory Usage: 15 MB, less than 21.95%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        from collections import defaultdict
        self.lis = defaultdict(list)
        
    def levelOrder(self, root: Optional[TreeNode], dist=0) -> List[List[int]]:
        if not root:
            return
        self.lis[dist].append(root.val)
        self.levelOrder(root.left, dist + 1)
        self.levelOrder(root.right, dist + 1)
        return self.lis.values()