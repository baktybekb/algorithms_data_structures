from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n + m) time | O(1) space
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        prev = None
        one, two = list1, list2
        while one and two:
            if one.val <= two.val:
                if prev:
                    prev.next = one
                prev = one
                one = one.next
            else:
                if prev:
                    prev.next = two
                prev = two
                two = two.next
        prev.next = one if one else two
        return list1 if list1.val <= list2.val else list2

