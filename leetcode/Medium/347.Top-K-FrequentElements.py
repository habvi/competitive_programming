from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        v, _ = zip(*c.most_common(k))
        return list(v)
