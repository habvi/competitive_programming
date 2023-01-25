class Solution:
    def reverseBits(self, n: int) -> int:
        b = list(bin(n)[2:])
        a = ['0'] * (32 - len(b)) + b
        return int("".join(a[::-1]), 2)
