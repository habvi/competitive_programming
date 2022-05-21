# 44ms, 99.03%
# 14.5MB, 46.65%

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        ans = [""] * numRows
        i = 0
        back = False
        for c in s:
            if not back:
                ans[i] = "".join((ans[i], c))
                i += 1
                if i == numRows - 1:
                    back = True
            else:
                ans[i] = "".join((ans[i], c))
                i -= 1
                if i == 0:
                    back = False
        return "".join(ans)