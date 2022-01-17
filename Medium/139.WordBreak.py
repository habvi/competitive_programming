# Runtime: 63 ms, faster than 21.38% of Python3 online submissions for Word Break.
# Memory Usage: 14.4 MB, less than 72.16% of Python3 online submissions for Word Break.

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n + 1):
            for wd in wordDict:
                if len(wd) <= i:
                    if s[i-len(wd) : i] == wd:
                        dp[i] += dp[i - len(wd)]
        return dp[-1] > 0



# S = Solution()
# s = "leetcode"
# wordDict = ["leet","code"]
# s = "applepenapple"
# wordDict = ["apple","pen"]
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
# s = "abcdef"
# wordDict = ["ab","abc","def"]
# s = "bb"
# wordDict = ["a","b","bbb","bbbb"]
# s = 'a'
# wordDict = ["a"]
# s = "dogs"
# wordDict = ["dog","s","gs"]
# print(S.wordBreak(s, wordDict))