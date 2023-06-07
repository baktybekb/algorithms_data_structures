# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n + m) time | O(1) space
def mergingLinkedLists(linkedListOne, linkedListTwo):
    node_one = linkedListOne
    node_two = linkedListTwo
    while node_two is not node_one:
        if node_one is None:
            node_one = linkedListTwo
        else:
            node_one = node_one.next
        if node_two is None:
            node_two = linkedListOne
        else:
            node_two = node_two.next
    return node_two
