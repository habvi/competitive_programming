# 40ms, 26.75%
# 14.4MB, 36.71%

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pr_l = ("{", "(", "[")
        pr_r = ("}", ")", "]")
        dq = []
        for k in s:
            if k in pr_l:
                dq.append(k)
            else:
                if len(dq) == 0:
                    return False
                if dq[-1] != pr_l[pr_r.index(k)]:
                    return False
                dq.pop()
        if dq:
            return False
        else:
            return True