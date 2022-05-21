def div_lis(x):
    div_l, div_r = [], []
    for i in range(1, int(x**0.5) + 1):
        if x % i != 0: continue
        div_l.append(i)
        if i != x // i:
            div_r.append(x // i)
    div = div_l + div_r[::-1]
    return div

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n <= k:
        print(1)
        continue
    div = div_lis(n)
    for d in div:
        if n // d <= k:
            print(d)
            break