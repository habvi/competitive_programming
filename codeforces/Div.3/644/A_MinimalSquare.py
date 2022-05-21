t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    m = max(min(a, b) * 2, max(a, b))
    print(m * m)