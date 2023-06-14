# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(max(n, m)) time | O(max(n, m)) space
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    dummy = LinkedList(0)
    current_node = dummy
    carry = 0
    node_one = linkedListOne
    node_two = linkedListTwo
    while node_one or node_two or carry != 0:
        value_one = node_one.value if node_one else 0
        value_two = node_two.value if node_two else 0
        values_sum = value_one + value_two + carry

        current_node.next = LinkedList(values_sum % 10)
        current_node = current_node.next
        carry = values_sum // 10
        node_one = node_one.next if node_one else None
        node_two = node_two.next if node_two else None
    return dummy.next
