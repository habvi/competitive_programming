t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) % n == 0:
        print(0)
    else:
        print(1)