# 35ms, 33.85%
# 14.4MB, 36.76%

class Solution:
    def isValid(self, s: str) -> bool:
        dq = []
        for k in s:
            if len(dq) and dq[-1] + k in ("{}", "()", "[]"):
                dq.pop()
                continue
            dq.append(k)
        return len(dq) == 0