from collections import Counter

a, b, c = map(int, input().split())

s = set([a, b, c])
if (n := len(s)) == 1:
    print(a)
elif n == 3:
    print(6 - a - b - c)
else:
    C = Counter([a, b, c])
    for d in (a, b, c):
        if C[d] == 1:
            print(d)
            exit()