# Runtime : 64ms, 90.70%
# Memory : 14.3MB, 73.60%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        now1, now2 = l1, l2
        s1, s2 = str(now1.val), str(now2.val)
        
        while now1:
            next1 = now1.next
            if next1:
                s1 += str(next1.val)
            now1 = next1

        while now2:
            next2 = now2.next
            if next2:
                s2 += str(next2.val)
            now2 = next2
        
        answer = str(int(s1[::-1]) + int(s2[::-1]))[::-1]
        
        res = dummy = ListNode(0)
        for ans in answer:
            res.next = ListNode(int(ans))
            res = res.next
        return dummy.next