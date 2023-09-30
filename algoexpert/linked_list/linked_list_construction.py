# https://www.algoexpert.io/questions/linked-list-construction

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
        else:
            self.head = node
            self.tail = node

    def setTail(self, node):
        if self.tail:
            self.insertAfter(self.tail, node)
        else:
            self.setHead(node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        if node.prev:
            node.prev.next = nodeToInsert
        else:
            self.head = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next:
            node.next.prev = nodeToInsert
        else:
            self.tail = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        cur_position = 1
        node = self.head
        while cur_position != position:
            node = node.next
            cur_position += 1
        if node:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setHead(nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node:
            next_node = node.next
            if node.value == value:
                self.remove(node)
            node = next_node

    def remove(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        self.remove_links(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def remove_links(self, node):
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        node.prev = None
        node.next = None


