class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = []
        for c in s:
            if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
                t.append(c.lower())
        a = "".join(t)
        return a == a[::-1]
