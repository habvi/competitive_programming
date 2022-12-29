from math import comb

class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        for two in range(n // 2 + 1):
            one = n - 2 * two
            ans += comb(one + two, one)
        return ans
