# Runtime: 129 ms, faster than 60.16%
# Memory Usage: 18.5 MB, less than 92.08% 

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        n = len(preorder)
        def dfs(l, r):
            if l > r:
                return None
            root_val = preorder[i[0]]
            root = TreeNode(root_val)
            i[0] += 1
            
            m = inorder.index(root_val)
            root.left = dfs(l, m - 1)
            root.right = dfs(m + 1, r)
            return root
        i = [0]
        return dfs(0, n - 1)

# S = Solution()
# a = [1, 2, 4, 5, 6, 3, 7, 9, 8, 10, 11]
# b = [4, 2, 5, 6, 1, 9, 7, 3, 10, 8, 11]
# print(S.buildTree(a, b))