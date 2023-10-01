# https://www.algoexpert.io/questions/merge-linked-lists

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n + m) time | O(1) space
def mergeLinkedLists(headOne, headTwo):
    one, two = headOne, headTwo
    prev = None
    while one and two:
        if one.value <= two.value:
            if prev:
                prev.next = one
            prev = one
            one = one.next
        else:
            if prev:
                prev.next = two
            prev = two
            two = two.next
    prev.next = one if one else two
    return headOne if headOne.value <= headTwo.value else headTwo
