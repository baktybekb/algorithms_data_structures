# https://www.algoexpert.io/questions/reverse-linked-list

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def reverseLinkedList(head):
    node = head
    prev = None
    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp
    return prev
