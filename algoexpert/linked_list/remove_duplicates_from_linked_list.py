# https://www.algoexpert.io/questions/remove-duplicates-from-linked-list

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeDuplicatesFromLinkedList(head):
    node = head
    while node:
        while node.next and node.value == node.next.value:
            node.next = node.next.next
        node = node.next
    return head

