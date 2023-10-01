# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def findLoop(head):
    low = fast = head
    while True:
        low = low.next
        fast = fast.next.next
        if low == fast:
            break
    low = head
    while low != fast:
        low = low.next
        fast = fast.next
    return low

