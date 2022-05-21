# Runtime: 52 ms, faster than 25.89%
# Memory Usage: 16.4 MB, less than 52.74%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=-float('inf'), high=float('inf')) -> bool:        
        if (not root.left) and (not root.right):
            return True
        
        res = True
        if root.left:
            if low < root.left.val < root.val:
                res &= self.isValidBST(root.left, low, root.val)
            else:
                res &= False
        
        if root.right:
            if root.val < root.right.val < high:
                res &= self.isValidBST(root.right, root.val, high)
            else:
                res &= False
        return res

# True  [2,1,3]
# False [5,1,4,null,null,3,6]
# False [5,4,6,null,null,3,7]
# True  [3,1,5,0,2,4,6]
# false [32,26,47,19,null,null,56,null,27]
# false [120,70,140,50,100,130,160,20,55,75,110,119,135,150,200]