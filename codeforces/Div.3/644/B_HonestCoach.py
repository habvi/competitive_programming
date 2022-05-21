t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    ans = float('inf')
    for i in range(n - 1):
        ans = min(ans, s[i + 1] - s[i])
    print(ans)