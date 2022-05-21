t = int(input())
for _ in range(t):
    n, l = map(int, input().split()) 
    X = list(map(int, input().split()))
    if len(set(X)) == 1:
        print(X[0])
        continue

    mx = max(X)
    lmx = len(bin(mx)) - 2
    cnt = [0] * lmx
    for x in X:
        for i in range(lmx):
            if x>>i & 1 == 0:
                cnt[i] += 1
    
    ans = 0
    mn = n // 2 if n % 2 else n // 2 - 1
    for i in range(lmx):
        if cnt[i] <= mn:
            ans |= 1 << i
    print(ans)