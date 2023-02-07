from heapq import heappop, heappush

class MedianFinder:
    def __init__(self):
        self.min_hq = []
        self.max_hq = []
        self.total = 0

    def addNum(self, num: int) -> None:
        self.total += 1
        if self.max_hq and num < -self.max_hq[0]:
            heappush(self.max_hq, -num)
        elif self.min_hq and num > self.min_hq[0]:
            heappush(self.min_hq, num)
        else:
            heappush(self.max_hq, -num)

        if len(self.min_hq) > len(self.max_hq):
            heappush(self.max_hq, -heappop(self.min_hq))
        if len(self.min_hq) + 1 < len(self.max_hq):
            heappush(self.min_hq, -heappop(self.max_hq))

    def findMedian(self) -> float:
        if self.total % 2:
            return -self.max_hq[0]
        else:
            return (-self.max_hq[0] + self.min_hq[0]) / 2


'''
always len(max_hq) >= len(min_hq)
max : -10 -7 -5
min : 2 3
'''

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
