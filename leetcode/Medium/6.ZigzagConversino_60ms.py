# 60ms, 71.52%
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
            if back and i == 0:
                back = False
            if i == numRows - 1:
                back = True

            ans[i] = "".join((ans[i], c))
            if back:
                i -= 1
                continue
            i += 1
        return "".join(ans)