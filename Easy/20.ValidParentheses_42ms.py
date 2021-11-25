# 42ms, 23.76%
# 14.2MB, 65.64%

class Solution:
    def isValid(self, s: str) -> bool:
        dq = []
        for k in s:
            if dq:
                if dq[-1] + k in ("{}", "()", "[]"):
                    dq.pop()
                else:
                    dq.append(k)
            else:
                dq.append(k)
        if dq: return False
        else: return True