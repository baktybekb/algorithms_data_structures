from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time | O(1) space
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy
        while True:
            kth = self.get_kth(prev_group, k)
            if kth is None:
                break
            prev, curr = kth.next, prev_group.next
            while prev != kth:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp
        return dummy.next

    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
