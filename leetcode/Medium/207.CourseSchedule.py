from collections import defaultdict
from heapq import heappop, heappush
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        in_deg = defaultdict(int)
        for a, b in prerequisites:
            g[a].append(b)
            in_deg[b] += 1

        hq = []
        for i in range(numCourses):
            if not in_deg[i]:
                heappush(hq, i)

        ans = []
        while hq:
            v = heappop(hq)
            ans.append(v + 1)
            for nv in g[v]:
                in_deg[nv] -= 1
                if not in_deg[nv]:
                    heappush(hq, nv)
        return len(ans) == numCourses


S = Solution()
print(S.canFinish(2, [[1, 0], [0, 1]]))
print(S.canFinish(1, []))
print(S.canFinish(2, [[0, 1]]))