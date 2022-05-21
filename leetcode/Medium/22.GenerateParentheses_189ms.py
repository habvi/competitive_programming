# bit Bruto Force
# 189ms, 5.04%
# 14.7MB, 41.49%

class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        n *= 2
        for i in range(1<<n):
            s = ""
            cnt = 0
            for j in range(n):
                if cnt < 0:
                    break
                if i & (1<<j):
                    s += "("
                    cnt += 1
                else:
                    s += ")"
                    cnt -= 1
            else:
                if cnt == 0:
                    ans.append(s)
        return ans