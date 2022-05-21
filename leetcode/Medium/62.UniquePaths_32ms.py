# Runtime: 32 ms, faster than 65.44% 
# Memory Usage: 14.3 MB, less than 66.60%

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import factorial
        return (factorial(m + n - 2) // factorial(m - 1) // factorial(n - 1))