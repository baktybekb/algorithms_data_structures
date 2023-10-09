from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n * log(k)) time | O(n) space
# n --> average length of each list, k --> number of lists
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.merge(l1, l2))
            lists = merged
        return lists[0]

    def merge(self, list_one, list_two, prev=None):
        if not list_one or not list_two:
            return list_one if list_one else list_two
        one = list_one
        two = list_two
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
        return list_one if list_one.val <= list_two.val else list_two
