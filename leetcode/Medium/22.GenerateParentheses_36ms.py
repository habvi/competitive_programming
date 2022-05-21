# Recursion
# 36ms, 70.14%
# 14.7MB, 41.47%

import sys
sys.setrecursionlimit(10**7)

class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        def dfs(s = ['('], left = 1, right = 0):
            if left + right == n * 2:
                ans.append("".join(s))
                return
            if left < n:
                s.append('(')
                dfs(s, left + 1, right)
                s.pop()
            if left > right:
                s.append(')')
                dfs(s, left, right + 1)
                s.pop()
        dfs()
        return ans