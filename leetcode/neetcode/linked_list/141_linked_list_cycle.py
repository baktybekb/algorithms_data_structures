from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# O(n) time | O(1) space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

