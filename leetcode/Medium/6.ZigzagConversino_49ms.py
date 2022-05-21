# 49ms, 91.90%
# 14.1MB, 96.77%

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        ans = [""] * numRows
        i = 0
        back = False
        for c in s:
            ans[i] = "".join((ans[i], c))
            if not back:
                i += 1
                if i == numRows - 1:
                    back = True
            else:
                i -= 1
                if i == 0:
                    back = False
        return "".join(ans)