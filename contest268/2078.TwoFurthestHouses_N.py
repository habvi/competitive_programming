# Runtime : 36ms
# Memory : 14.3MB

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        if colors[0] != colors[-1]:
            return n - 1
        
        answer = 0
        for i in range(1, n-1):
            if colors[i] == colors[0]:
                continue
            answer = max(answer, i)
            answer = max(answer, n - i - 1)
        return answer
