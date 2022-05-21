# Runtime : 68m, 59.35%
# Memory : 14.3MB, 55.75%
# two pointers

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        selected = set()
        right = 0
        answer = 0
        for left in range(n):
            while right < n and s[right] not in selected:
                selected.add(s[right])
                right += 1
                
            answer = max(answer, len(selected))
            if left == right:
                right += 1
            else:
                selected.remove(s[left])
        return answer