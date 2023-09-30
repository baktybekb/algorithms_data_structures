# https://www.algoexpert.io/questions/remove-kth-node-from-end

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
    l = r = head
    for i in range(k):
        r = r.next
    if r is None:
        head.value = head.next.value
        head.next = head.next.next
        return head
    while r and r.next:
        l = l.next
        r = r.next
    l.next = l.next.next
    return head
