T = int(input())
for _ in range(T):
    n, R, B = map(int, input().split())
    div, mod = divmod(R, B + 1)
    ans = []
    for i in range(B * 2 + 1):
        if i % 2:
            ans.append('B')
        else:
            if mod:
                ans.append('R' * (div + 1))
                mod -= 1
            else:
                ans.append('R' * div)
    print(''.join(ans))