# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def shiftLinkedList(head, k):
    length = 0
    node = head
    while node:
        length += 1
        node = node.next

    k = k % length
    if k == 0:
        return head

    one = two = head
    for i in range(k):
        two = two.next
    while two and two.next:
        one, two = one.next, two.next

    temp = one.next
    one.next = None
    two.next = head
    return temp

