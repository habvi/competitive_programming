class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_1 = len(text1)
        len_2 = len(text2)
        dp = [[0] * (len_2 + 1) for _ in range(len_1 + 1)]
        for i in range(len_1 + 1):
            for j in range(len_2 + 1):
                if i < len_1 and j < len_2:
                    if text1[i] == text2[j]:
                        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
                if i < len_1:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
                if j < len_2:
                    dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])
        return dp[-1][-1]