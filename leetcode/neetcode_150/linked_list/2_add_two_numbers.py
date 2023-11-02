from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(max(n, m)) time | O(max(n, m)) space
class Solution:
    def addTwoNumbers(self, one: Optional[ListNode], two: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        new = ListNode(0)
        node = new
        while one or two or remainder:
            one_val = one.val if one else 0
            two_val = two.val if two else 0
            cur_sum = one_val + two_val + remainder
            if cur_sum >= 10:
                remainder = 1
                cur_sum %= 10
            else:
                remainder = 0
            node.next = ListNode(cur_sum)
            node = node.next
            one = one.next if one else None
            two = two.next if two else None
        return new.next
