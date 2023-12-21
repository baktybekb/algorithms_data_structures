# https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(min(n, m)) time | O(1) space
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        pointer1, pointer2, previous = list1, list2, None
        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                if previous:
                    previous.next = pointer1
                previous = pointer1
                pointer1 = pointer1.next
            else:
                if previous:
                    previous.next = pointer2
                previous = pointer2
                pointer2 = pointer2.next
        if pointer1:
            previous.next = pointer1
        elif pointer2:
            previous.next = pointer2
        return list1 if list1.val <= list2.val else list2
