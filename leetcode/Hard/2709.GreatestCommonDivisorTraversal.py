import sys
sys.setrecursionlimit(10 ** 7)
from itertools import combinations
from collections import defaultdict

# 7754ms

class Solution:
    def canTraverseAllPairs(self, nums) -> bool:
        def sieve(x):
            memo = [0] * (x + 1)
            primes = []
            for i in range(2, x + 1):
                if memo[i]:
                    continue
                primes.append(i)
                memo[i] = i
                for j in range(i * i, x + 1, i):
                    if memo[j]:
                        continue
                    memo[j] = i
            return memo, primes


        def get_pfact(x):
            pfact = []
            while x > 1:
                pfact.append(memo[x])
                x //= memo[x]
            return pfact


        def root(x):
            if rank[x] < 0:
                return x
            rank[x] = root(rank[x])
            return rank[x]
        def unite(x, y):
            x, y = root(x), root(y)
            if x == y:
                return False
            if rank[x] > rank[y]:
                x, y = y, x
            rank[x] += rank[y]
            rank[y] = x
            return True
        def is_same(x, y):
            return root(x) == root(y)


        if nums == [1]:
            return True
        nums = set(nums)
        if 1 in nums:
            return False
        memo, _ = sieve(10**5 + 5)
        rank = defaultdict(lambda : -1)
        all_pfact = set()
        for x in nums:
            pfact = set(get_pfact(x))
            all_pfact |= pfact
            for (a, b) in combinations(list(pfact), 2):
                unite(a, b)

        all_pfact = list(all_pfact)
        for i in range(len(all_pfact) - 1):
            if not is_same(all_pfact[i], all_pfact[i + 1]):
                return False
        return True



S = Solution()
print(S.canTraverseAllPairs([4, 3, 12, 8]))
print(S.canTraverseAllPairs([42,40,45,42,50,33,30,45,33,45,30,36,44,1,21,10,40,42,42]))
print(S.canTraverseAllPairs([1]))
print(S.canTraverseAllPairs([1, 1]))
