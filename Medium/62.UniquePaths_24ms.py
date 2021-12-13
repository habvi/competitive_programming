# Runtime: 24 ms, faster than 96.46%
# Memory Usage: 14.3 MB, less than 38.60%

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        fact = [1]
        a = 1
        for i in range(2, m + n):
            fact.append(a)
            a *= i
        return fact[m + n - 2] // fact[m - 1] // fact[n - 1]