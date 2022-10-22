N = int(input())

A = input().split('=')
ans = set()
for a in A:
    ans.add(eval(a))
print("Yes" if len(ans) == 1 else "No")