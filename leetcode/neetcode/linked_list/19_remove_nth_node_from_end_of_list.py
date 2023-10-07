from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time | O(1) space
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = r = head
        for _ in range(n):
            r = r.next
        if r is None:
            return head.next
        while r and r.next:
            l = l.next
            r = r.next
        l.next = l.next.next
        return head
