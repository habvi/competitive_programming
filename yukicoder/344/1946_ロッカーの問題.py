def div_lis(x):
    div_l, div_r = [], []
    i = 1
    while i * i <= x:
        if x % i == 0:
            div_l.append(i)
            if i != x // i:
                div_r.append(x // i)
        i += 1
    div = div_l + div_r[::-1]
    return div


n, m = map(int, input().split())
A = set(map(int, input().split()))

open_ = [0] * (n + 1)
ans = 0
for x in reversed(range(1, n + 1)):
    if (x in A) != open_[x]:
        for div in div_lis(x):
            open_[div] ^= 1
    else:
        ans += 1

print(ans)