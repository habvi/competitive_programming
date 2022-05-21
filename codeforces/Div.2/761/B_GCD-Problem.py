t = int(input())
for _ in range(t):
    n = int(input())
    n -= 1
    if n % 2:
        a = n // 2
        b = a + 1
    else:
        m = n // 2
        if m % 2:
            a = m - 2
            b = m + 2
        else:
            a = m - 1
            b = m + 1
    print(a, b, 1)