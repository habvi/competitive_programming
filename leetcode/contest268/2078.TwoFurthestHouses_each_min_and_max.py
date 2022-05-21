# Runtime : 204ms
# Memory : 14.2MB

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        MAX = 1000
        min_c = [MAX] * 101
        max_c = [-1] * 101
        for i in range(n):
            min_c[colors[i]] = min(min_c[colors[i]], i)
            max_c[colors[i]] = max(max_c[colors[i]], i)

        answer = 0
        for i in range(101):
            for j in range(101):
                if i == j:
                    continue
                if min_c[i] < MAX and min_c[j] < MAX:
                    answer = max(answer, abs(min_c[i] - min_c[j]))
                if max_c[i] != -1 and max_c[j] != -1:
                    answer = max(answer, abs(max_c[i] - max_c[j]))
                if min_c[i] < MAX and max_c[j] != -1:
                   answer = max(answer, abs(min_c[i] - max_c[j]))
        return answer