# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    ans = ''
    for k in s:
        if k == 'E':
            ans += 'S'
        else:
            ans += 'E'
    print('Case #{}:'.format(i + 1), ans)