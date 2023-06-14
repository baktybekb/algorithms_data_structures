# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    prev, cur = None, head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev
