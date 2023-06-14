# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList):
    current_node = linkedList
    while current_node:
        next_distinct_node = current_node.next
        while next_distinct_node and next_distinct_node.value == current_node.value:
            next_distinct_node = next_distinct_node.next
        current_node.next = next_distinct_node
        current_node = next_distinct_node
    return linkedList
