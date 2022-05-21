# Runtime: 62 ms, faster than 11.50%
# Memory Usage: 14.4 MB, less than 26.56%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        from collections import defaultdict
        cnt = defaultdict(int)
        nxt = head
        while nxt:
            cnt[nxt.val] += 1
            nxt = nxt.next
        
        res = dummy = ListNode(0)
        for k, v in cnt.items():
            if v == 1:
                res.next = ListNode(k)
                res = res.next
        return dummy.next