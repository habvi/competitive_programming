# Runtime: 84 ms, faster than 99.26% of Python3 online submissions for Group Anagrams.
# Memory Usage: 18.2 MB, less than 39.34% of Python3 online submissions for Group Anagrams.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        for st in strs:
            d[tuple(sorted(st))].append(st)
        return d.values()

# S = Solution()
# a = ["eat","tea","tan","ate","nat","bat"]
# print(S.groupAnagrams(a))