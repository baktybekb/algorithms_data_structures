# https://leetcode.com/problems/reverse-linked-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time | O(1) space
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        node = head
        while node:
            temp = node.next
            node.next = previous
            previous = node
            node = temp
        return previous

