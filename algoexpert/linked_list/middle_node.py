# https://www.algoexpert.io/questions/middle-node

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def middleNode(head):
    low = fast = head
    while fast and fast.next:
        low = low.next
        fast = fast.next.next
    return low

