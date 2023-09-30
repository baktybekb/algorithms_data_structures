# https://www.algoexpert.io/questions/sum-of-linked-lists

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(max(n, m)) time | O(max(n, m)) space
def sumOfLinkedLists(one, two):
    new_list = LinkedList(None)
    node = new_list
    remainder = 0
    while one or two or remainder:
        one_val = one.value if one else 0
        two_val = two.value if two else 0
        val = one_val + two_val + remainder
        if val > 9:
            remainder = 1
            val = val % 10
        else:
            remainder = 0
        node.next = LinkedList(val)
        node = node.next
        one = one.next if one else None
        two = two.next if two else None
    return new_list.next


