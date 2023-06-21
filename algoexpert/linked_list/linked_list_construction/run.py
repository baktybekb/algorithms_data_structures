# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head:
            self.insertBefore(self.head, node)
            return
        self.head = node
        self.tail = node

    def setTail(self, node):
        if self.tail:
            self.insertAfter(self.tail, node)
            return
        self.setHead(node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        cur_position = 1
        node = self.head
        while node and cur_position != position:
            node = node.next
            cur_position += 1
        if node:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node:
            next_node = node.next
            if node.value == value:
                self.remove(node)
            node = next_node

    def remove(self, node):
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev
        self.remove_bindings(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node and node.value != value:
            node = node.next
        return node is not None

    def remove_bindings(self, node):
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        node.prev = None
        node.next = None


def test_doubly_linked_list():
    # Create a new doubly linked list
    dll = DoublyLinkedList()

    # Create some nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # Test setHead method
    dll.setHead(node1)
    assert dll.head == node1
    assert dll.tail == node1

    # Test setTail method
    dll.setTail(node2)
    assert dll.head == node1
    assert dll.tail == node2
    assert dll.head.next == node2
    assert dll.tail.prev == node1

    # Test insertBefore method
    dll.insertBefore(node2, node3)
    assert dll.head == node1
    assert dll.head.next == node3
    assert dll.tail == node2
    assert dll.tail.prev == node3

    # Test insertAfter method
    dll.insertAfter(node3, node4)
    assert dll.head == node1
    assert dll.head.next == node3
    assert node3.next == node4
    assert dll.tail == node2
    assert dll.tail.prev == node4

    # Test insertAtPosition method
    node5 = Node(5)
    dll.insertAtPosition(1, node5)
    assert dll.head == node5
    assert dll.head.next == node1
    assert node1.prev == node5

    # Test removeNodesWithValue method
    dll.removeNodesWithValue(1)
    assert dll.head == node5
    assert dll.head.next == node3

    # Test containsNodeWithValue method
    assert dll.containsNodeWithValue(5)
    assert not dll.containsNodeWithValue(1)

    print("All test cases pass")


if __name__ == '__main__':
    test_doubly_linked_list()
