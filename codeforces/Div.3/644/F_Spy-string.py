t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [input() for _ in range(n)]
    ans = 0
    en = False
    for si in range(n):
        for i in range(m):
            for j in range(26):
                ls = list(a[si])
                ch = chr(ord('a') + j)
                if ls[i] == ch:
                    continue
                ls[i] = ch
                t = "".join(ls)
                
                tot = 0
                for sj in range(n):
                    if si == sj:
                        continue
                    cnt = 0
                    for s1, s2 in zip(t, a[sj]):
                        if s1 == s2:
                            cnt += 1
                    if cnt in (m, m - 1):
                        tot += 1
                if tot == n - 1:
                    print(t)
                    en = True
                    break
            if en:
                break
        if en:
            break
    if en:
        continue
    print(-1)