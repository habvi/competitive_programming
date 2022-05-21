n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    x = a - b
    if x == 0:
        print('=')
    elif str(x)[0] == '-':
        print(chr(60))
    else:
        print(chr(62))