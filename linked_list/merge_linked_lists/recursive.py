# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n + m) time | O(n + m) space
def mergeLinkedLists(headOne, headTwo):
    helper(None, headOne, headTwo)
    if headOne.value <= headTwo.value:
        return headOne
    return headTwo


def helper(prev, p1, p2):
    if p1 is None:
        prev.next = p2
        return
    if p2 is None:
        return
    if p1.value > p2.value:
        if prev:
            prev.next = p2
        temp = p2.next
        p2.next = p1
        helper(p2, p1, temp)
    else:
        helper(p1, p1.next, p2)


