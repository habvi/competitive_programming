# Runtime : 1476ms, 100%
# Memory : 54.2MB

from collections import defaultdict
from bisect import bisect, bisect_left

class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.counts = defaultdict(list)
        
        for i, elem in enumerate(arr):
            self.counts[elem].append(i)

        for k, v in self.counts.items():
            v.sort()

    def query(self, left: int, right: int, value: int) -> int:
        values = self.counts[value]
        answer = bisect(values, right) - bisect_left(values, left)
        return answer

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
