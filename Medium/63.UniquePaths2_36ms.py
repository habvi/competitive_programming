# Runtime: 36 ms, faster than 94.72%
# Memory Usage: 14.5 MB, less than 35.83%

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[h -1][w - 1]:
            return 0
        
        cnt = [[0] * (w + 1) for _ in range(h + 1)]
        cnt[0][0] = 1
        for i in range(h):
            for j in range(w):
                if obstacleGrid[i][j]:
                    continue
                cnt[i + 1][j] += cnt[i][j]
                cnt[i][j + 1] += cnt[i][j]
        return cnt[h - 1][w - 1]