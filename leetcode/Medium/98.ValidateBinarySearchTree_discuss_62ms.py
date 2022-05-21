# Runtime: 62 ms, faster than 16.01%
# Memory Usage: 17.8 MB, less than 7.17%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
        if not root.left and not root.right:
            return True
        
        lis = []
        def orderBST(root):
            if root:
                orderBST(root.left)
                lis.append(root.val)
                orderBST(root.right)
        orderBST(root)

        if lis == list(sorted(set(lis))):
            return True
        else:
            return False
