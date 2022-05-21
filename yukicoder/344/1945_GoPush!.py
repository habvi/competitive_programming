n = int(input())
A = list(map(int, input().split()))

xor = 0
for a in A:
    xor ^= a

print('First' if xor else 'Second')