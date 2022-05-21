# Runtime: 48 ms, faster than 24.77%
# Memory Usage: 14.3 MB, less than 24.97%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = set()
        nxt = head
        while nxt:
            cnt.add(nxt.val)
            nxt = nxt.next
        cnt = sorted(list(cnt))
        
        res = dummy = ListNode(0)
        for ans in cnt:
            res.next = ListNode(ans)
            res = res.next
        return dummy.next