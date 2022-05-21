n = int(input())
S = input()

ans = 0
for i, s in enumerate(S, 1):
    if s in "ATGC":
        ans = i
print(ans)