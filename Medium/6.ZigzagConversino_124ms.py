# 124ms, 14.37%
# 14.2MB, 88.10%

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        ans = [""] * numRows
        i = 0
        back = False
        for j in range(n):
            if back and i == 0:
                back = False
            if i == numRows - 1:
                back = True

            ans[i] = "".join((ans[i], s[j]))
            if back:
                i = max(0, i - 1)
                continue
            i += 1
        return "".join(ans)