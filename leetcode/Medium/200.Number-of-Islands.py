# Runtime: 320 ms, faster than 74.78% of Python3 online submissions for Number of Islands.
# Memory Usage: 16.3 MB, less than 99.44% of Python3 online submissions for Number of Islands.

class Solution:
    def numIslands(self, grid) -> int:
        from collections import deque
        
        def bfs(sy, sx):
            q = deque([])
            q.append((sy, sx))
            while q:
                y, x = q.popleft()
                for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
                    ny, nx = y + dy, x + dx
                    if not (0 <= ny < h and 0 <= nx < w) or grid[ny][nx] == '0':
                        continue
                    if seen[ny][nx]:
                        continue
                    seen[ny][nx] = 1
                    q.append((ny, nx))

        h = len(grid)
        w = len(grid[0])    
        seen = [[0] * w for _ in range(h)]
        ans = 0
        for i in range(h):
            for j in range(w):
                if seen[i][j] or grid[i][j] == '0':
                    continue
                bfs(i, j)
                ans += 1
        return ans
        

# S = Solution()  
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# print(S.numIslands(grid))