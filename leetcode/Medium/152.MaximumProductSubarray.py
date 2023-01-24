from itertools import accumulate
from operator import mul

class Solution:
    def maxProduct(self, nums) -> int:
        A, B = [], []
        is_zero = False
        for x in nums:
            if x == 0:
                if B:
                    A.append(B)
                B = []
                is_zero = True
            else:
                B.append(x)
        if B:
            A.append(B)

        ans = -float('inf') if not is_zero else 0
        for B in A:
            ac = list(accumulate(B, mul))
            minus_min = None if ac[0] >= 0 else ac[0]
            total = ac[0]
            for a in ac[1:]:
                if a < 0:
                    if minus_min is None:
                        minus_min = a
                    else:
                        total = max(total, a // minus_min)
                else:
                    total = max(total, a)
            ans = max(ans, total)
        return ans

S = Solution()
print(S.maxProduct([2, 3, -2, 4]))
print(S.maxProduct([-2, 0, -1]))
print(S.maxProduct([0]))
print(S.maxProduct([-2, 0]))
print(S.maxProduct([3, -1, 4]))
print(S.maxProduct([1, 0, -1, 2, 3, -5, -2])) # -1 -2 -6 30 -60
print(S.maxProduct([-2]))
