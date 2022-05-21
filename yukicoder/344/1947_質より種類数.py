n, V, C = map(int, input().split())
vw = [tuple(map(int, input().split())) for _ in range(n)]

INF = float('inf')
ndp = [-INF] * (V + 1)
ndp[0] = 0

for v, w in vw:
    dp = ndp[:]
    for i in range(V + 1):
        if i + v <= V:
            ndp[i + v] = max(ndp[i + v], dp[i] + w + C)
    for i in range(V + 1):
        if i + v <= V:
            ndp[i + v] = max(ndp[i + v], ndp[i] + w)

print(max(ndp))