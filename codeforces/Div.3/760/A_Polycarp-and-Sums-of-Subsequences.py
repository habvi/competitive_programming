from itertools import combinations
t = int(input())
for _ in range(t):
    A = list(map(int, input().split()))
    for a, b, c in combinations(A, 3):
        B = [a, b, c, a + b, a + c, b + c, a + b + c]
        B.sort()
        if A == B:
            print(a, b, c)
            break