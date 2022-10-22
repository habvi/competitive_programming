from collections import defaultdict

N, p, q = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N)]

score = defaultdict(list)
for i, (a, b) in enumerate(ab):
    s = p * a + q * b
    score[s].append(i)

ans = [None] * N
total = 0
for k in sorted(score.keys(), reverse=True):
    for v in score[k]:
        ans[v] = total + 1
    total += len(score[k])
print(*ans)
