from collections import defaultdict
from math import comb

def dfs(x, i, A, res, ans):
    if i == len(A):
        res[x] += ans
        res[x] %= MOD
        return
    for leg in range(11):
        a, b = A[i]
        dfs(x + a * leg, i + 1, A, res, ans * comb(10, leg) % MOD)
        dfs(x + a * leg + b, i + 1, A, res, ans * comb(10, leg) % MOD)

def calc(A):
    res = defaultdict(int)
    dfs(0, 0, A, res, 1)
    return res


N = int(input())
ab = [tuple(map(int, input().split())) for _ in range(N)]
MOD = 998244353

total = sum(a * 10 + b for a, b in ab)
if total % 2:
    print(0)
    exit()
total //= 2

mid = N // 2
crab1 = calc(ab[:mid])
crab2 = calc(ab[mid:])

ans = 0
for k, v1 in crab1.items():
    v2 = crab2[total - k]
    ans += v1 * v2
    ans %= MOD
print(ans)