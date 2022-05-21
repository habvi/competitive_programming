from collections import defaultdict
from itertools import count

*V, n = map(int, input().split())

now = [0] * 5
now[0] = V[0]

idx = defaultdict(lambda : -1)
route = []

for i in count():
    idx[tuple(now)] = i
    route.append(now[:4])

    l, r = i % 4, (i + 1) % 4
    move = min(now[l], V[r] - now[r])
    now[l] -= move
    now[r] += move
    now[4] = (now[4] + 1) % 4 

    if tuple(now) in idx:
        break

loop = idx[tuple(now)]

if n < loop:
    print(*route[n])
else:
    route = route[loop:]
    n -= loop
    print(*route[n % len(route)])