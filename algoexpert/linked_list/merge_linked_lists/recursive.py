# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n + m) time | O(n + m) space
def mergeLinkedLists(headOne, headTwo):
    helper(headOne, headTwo, None)
    return headOne if headOne.value <= headTwo.value else headTwo


def helper(one, two, prev):
    if not one or not two:
        prev.next = one if one else two
        return
    if one.value <= two.value:
        if prev:
            prev.next = one
        return helper(one.next, two, one)
    else:
        if prev:
            prev.next = two
        return helper(one, two.next, two)
