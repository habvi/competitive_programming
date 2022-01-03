# Runtime: 456 ms, faster than 97.45%
# Memory Usage: 49.1 MB, less than 70.92%

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) -> int:
        from collections import deque
        if not root:
            return 0
        que = deque([root])
        depth = 0
        while que:
            depth += 1
            for i in range(len(que)):
                par = que.popleft()
                if not par.left and not par.right:
                    return depth
                if par.left:
                    que.append(par.left)
                if par.right:
                    que.append(par.right)
                       