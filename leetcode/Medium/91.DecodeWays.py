class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = (s[0] != '0')
        for i in range(n + 1):
            if i - 1 >= 0 and s[i - 1] != '0':
                x = int(s[i - 1:i])
                if 1 <= x <= 26:
                    dp[i] += dp[i - 1]
            if i - 2 >= 0 and s[i - 2] != '0':
                x = int(s[i - 2:i])
                if 1 <= x <= 26:
                    dp[i] += dp[i - 2]
        return dp[-1]

# TLE
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         def itoc(i):
#             return chr(i + ord('A'))

#         def dfs(decode, n, i):
#             print(decode, i)
#             if i == len(s):
#                 ans.add(''.join(decode))
#                 return
#             if s[i] != '0':
#                 if i + 1 <= n:
#                     x = int(s[i:i + 1])
#                     if 1 <= x <= 26:
#                         dfs(decode + [itoc(x - 1)], n, i + 1)
#                 if i + 2 <= n:
#                     x = int(s[i:i + 2])
#                     if 1 <= x <= 26:
#                         dfs(decode + [itoc(x - 1)], n, i + 2)

#         ans = set()
#         dfs([], len(s), 0)
#         return len(ans)


S = Solution()
print(S.numDecodings("12"))
print(S.numDecodings("226"))
print(S.numDecodings("06"))
print(S.numDecodings("111111111111111111111111111111111111111111111"))
print(S.numDecodings("2101"))
