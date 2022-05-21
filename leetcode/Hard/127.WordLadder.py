# Runtime: 425 ms, faster than 46.84% of Python3 online submissions for Word Ladder.
# Memory Usage: 26.6 MB, less than 5.16% of Python3 online submissions for Word Ladder.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        from collections import defaultdict, deque
        from itertools import combinations
        if endWord not in set(wordList):
            return 0
        
        wordList.append(beginWord)
        n = len(beginWord)
        g = defaultdict(lambda : set())
        
        def unite(word, words):
            for i in range(n):
                l_word = list(word)
                l_word[i] = '?'
                words.append("".join(l_word))
            for u, v in combinations(words, 2):
                g[u].add(v)
                g[v].add(u)
            
        for word in wordList:
            unite(word, [])
        unite(beginWord, [beginWord])
        unite(endWord, [endWord])
        
        dist = defaultdict(lambda : -1)
        dist[beginWord] = 0
        que = deque([])
        que.append(beginWord)
        while que:
            v = que.popleft()
            for nv in g[v]:
                if dist[nv] != -1:
                    continue
                dist[nv] = dist[v] + 1
                if nv == endWord:
                    return dist[nv]
                que.append(nv)
        return 0

# S = Solution()
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# print(S.ladderLength(beginWord, endWord, wordList))