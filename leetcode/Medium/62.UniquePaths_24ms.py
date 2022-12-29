from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = (m - 1) + (n - 1)
        return comb(total, m - 1)
