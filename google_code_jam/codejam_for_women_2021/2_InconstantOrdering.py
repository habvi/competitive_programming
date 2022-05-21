# https://codingcompetitions.withgoogle.com/codejamio/round/00000000004360f2/00000000007772ed

def output(i, ans):
    print(f'Case #{i + 1}: {ans}')


T = int(input())
for t in range(T):
    n = int(input())
    L = list(map(int, input().split()))

    ans = ['A']
    for i, m in enumerate(L):
        S = []
        if i % 2:
            for j in range(m):
                S.append(chr(j + ord('A')))
            S = S[::-1]

            change = chr(m + ord('A'))
            tail = ans[-1][-1]
            if tail <= change:
                ans[-1] = ans[-1][:-1] + change
        else:
            for j in range(1, m + 1):
                S.append(chr(j + ord('A')))

        ans.append(''.join(S))

    output(t, ''.join(ans))