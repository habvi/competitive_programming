# https://codingcompetitions.withgoogle.com/codejamio/round/00000000004360f2/0000000000777098

from collections import Counter

T = int(input())
for t in range(T):
    n = int(input())
    S = list(map(int, input().split()))

    c = Counter(S)
    ans = 0
    for i, num in enumerate(sorted(c.keys()), 1):
        ans += i * c[num]

    print(f'Case #{t + 1}: {ans}')