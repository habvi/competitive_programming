# Runtime: 32 ms, faster than 72.11%
# Memory Usage: 14.5 MB, less than 72.15%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.zigzag = []
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        que = deque([])
        que.append(root)
        pr = 0
        while que:
            res = []
            for _ in range(len(que)):
                v = que.popleft()
                res.append(v.val)
                if v.left:
                    que.append(v.left)
                if v.right:
                    que.append(v.right)
            if pr % 2 == 0:
                self.zigzag.append(res)
            else:
                self.zigzag.append(res[::-1])
            pr = 1 - pr
        return self.zigzag

# [1,2,3,4,null,null,5]   [[1],[3,2],[4,5]]