from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n + m) time | O(n + m) space
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        self.helper(list1, list2, None)
        return list1 if list1.val <= list2.val else list2

    def helper(self, one, two, prev):
        if not one or not two:
            if prev:
                prev.next = one if one else two
            return
        if one.val <= two.val:
            if prev:
                prev.next = one
            return self.helper(one.next, two, one)
        else:
            if prev:
                prev.next = two
            return self.helper(one, two.next, two)
