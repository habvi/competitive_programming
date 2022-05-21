# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231

t = int(input())
for i in range(t):
    n = input()

    a = ''
    for k in n:
        if k == '4':
            a += '3'
        else:
            a += k
    a = int(a)
    b = int(n) - a
    print('Case #{}:'.format(i + 1), a, b)