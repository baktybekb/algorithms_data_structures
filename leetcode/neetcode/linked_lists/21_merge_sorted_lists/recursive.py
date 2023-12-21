from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(min(n, m)) time | O(min(n, m)) space
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        self.helper(list1, list2, None)
        return list1 if list1.val <= list2.val else list2

    def helper(self, node1, node2, previous):
        if not node1 or not node2:
            previous.next = node1 if node1 else node2
            return
        if node1.val <= node2.val:
            if previous:
                previous.next = node1
            self.helper(node1.next, node2, node1)
        else:
            if previous:
                previous.next = node2
            self.helper(node1, node2.next, node2)
