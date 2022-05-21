t = int(input())
for _ in range(t):
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            if s[i][j] == '0':
                continue
            if not (s[i + 1][j] == '1' or s[i][j + 1] == '1'):
                print('NO')
                break
        else:
            continue
        break
    else:
        print('YES')
                     