# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n + m) time | O(1) space
def mergeLinkedLists(headOne, headTwo):
    prev = None
    p1 = headOne
    p2 = headTwo
    while p1 and p2:
        if p1.value > p2.value:
            if prev:
                prev.next = p2
            prev = p2
            p2 = p2.next
            prev.next = p1
        else:
            prev = p1
            p1 = p1.next
    if p1 is None:
        prev.next = p2
    if headOne.value <= headTwo.value:
        return headOne
    return headTwo



