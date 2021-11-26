# 28ms, 87.66%
# 14.4MB, 36.76%

class Solution:
    def isValid(self, s: str) -> bool:
        pr_l = "{(["
        pr_r = "})]"
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
        return len(dq) == 0