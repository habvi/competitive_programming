h, w = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(h)]

DXY = [(0, 1), (1, 0)]

dp = [[[0] * 2 for _ in range(w)] for _ in range(h)]
dp[0][0][0] = A[0][0]

for i in range(h):
    for j in range(w):
        a = dp[i][j][0]
        for di, dj in DXY:
            ni, nj = i + di, j + dj
            if not (0 <= ni < h and 0 <= nj < w):
                continue
            enemy = A[ni][nj]
            if a > enemy:
                dp[ni][nj][0] = max(dp[ni][nj][0], a + enemy)
            else:
                if dp[ni][nj][1]:
                    continue
                dp[ni][nj][1] = max(dp[ni][nj][0], a)

        a = dp[i][j][1]
        for di, dj in DXY:
            ni, nj = i + di, j + dj
            if not (0 <= ni < h and 0 <= nj < w):
                continue
            enemy = A[ni][nj]
            if a > enemy:
                dp[ni][nj][1] = max(dp[ni][nj][1], a + enemy)

if dp[-1][-1][0]:
    print('Yes')
else:
    ans = dp[-1][-1][1]
    print('Yes' if ans and ans > A[-1][-1] else 'No')