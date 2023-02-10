from typing import List
from collections import deque

def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs(seen, sy, sx):
        seen[sy][sx] = 1
        que = deque([])
        que.append((sy, sx))
        while que:
            y, x = que.popleft()
            for dy, dx in DXY:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < h and 0 <= nx < w) or seen[ny][nx]:
                    continue
                if heights[ny][nx] < heights[y][x]:
                    continue
                seen[ny][nx] = 1
                que.append((ny, nx))


    h = len(heights)
    w = len(heights[0])
    pacific = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if (i == 0 or j == 0) and not pacific[i][j]:
                bfs(pacific, i, j)

    atlantic = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if (i == h - 1 or j == w - 1) and not atlantic[i][j]:
                bfs(atlantic, i, j)

    ans = []
    for i in range(h):
        for j in range(w):
            if pacific[i][j] and atlantic[i][j]:
                ans.append([i, j])
    return ans


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(pacificAtlantic(heights))