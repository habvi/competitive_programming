# Runtime : 40ms
# Memory : 14.5MB

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        answer = 0
        res = capacity
        for i in range(n):
            if plants[i] <= res:
                res -= plants[i]
                answer += 1
                continue
            answer += 2*i + 1
            res = capacity
            res -= plants[i]
        return answer
