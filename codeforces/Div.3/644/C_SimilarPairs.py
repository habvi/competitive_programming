t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ev, od = [], []
    for a in A:
        if a % 2:
            od.append(a)
        else:
            ev.append(a)

    if len(od) % 2 == len(ev) % 2 == 0:
        print('YES')
        continue
    for e in ev:
        if e + 1 in od or e - 1 in od:
            print('YES')
            break
    else:
        print('NO')