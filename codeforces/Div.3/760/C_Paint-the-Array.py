from math import gcd
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    ok = True
    g = 0
    for i in range(0, n, 2):
        g = gcd(g, A[i])
    for i in range(1, n, 2):
        if A[i] % g == 0:
            ok = False
            break
    if ok:
        print(g)
        continue

    ok = True
    g = 0
    for i in range(1, n, 2):
        g = gcd(g, A[i])
    for i in range(0, n, 2):
        if A[i] % g == 0:
            ok = False
            break
    print(g if ok else 0)