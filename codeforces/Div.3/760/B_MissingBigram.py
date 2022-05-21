t = int(input())
for _ in range(t):
    n = int(input())
    s = input().split()
    ans = s[0][0]
    for i in range(n - 3):
        if s[i][-1] == s[i + 1][0]:
            ans += s[i][-1]
        else:
            ans += s[i][-1] + s[i + 1][0]
    ans += s[-1][-1]
    print(ans if len(ans) == n else ans + s[0][0])