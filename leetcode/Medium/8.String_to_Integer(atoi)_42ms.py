# 42ms, 24.70%
# 14.4MB, 26.03%

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip().split()
        if len(s) == 0:
            return 0

        s = s[0]
        n = len(s)
        head = s[0] if s[0] in "-+" else ""
        num = ""
        for i in range(len(head), n):
            if s[i].isdigit():
                num += s[i]
            else:
                break
        if not num:
            return 0

        hi = 2 ** 31 - 1
        lo = -2 ** 31
        num = int(("-" if head == "-" else "") + num)
        if num < lo:
            return max(lo, num)
        else:
            return min(hi, num)

# S = Solution()
# s = "+456"
# s = "-38646474848752928"
# s = "+aaaa"
# s = "aaaa"
# s = "-+12"
# s = "   +0  123"
# s = "790aaa"
# s = ""
# s = "  -42"
# s = "    0000000000026846"
# print(S.myAtoi(s))
