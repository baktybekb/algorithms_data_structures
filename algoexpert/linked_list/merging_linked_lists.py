# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n + m) time | O(1) space
def mergingLinkedLists(linkedListOne, linkedListTwo):
    one = linkedListOne
    two = linkedListTwo
    while one != two:
        one = one.next if one else linkedListTwo
        two = two.next if two else linkedListOne
    return one
