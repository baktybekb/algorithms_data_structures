"""Linked list"""


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, node: Node):
        if self.head:
            self.insert_before(self.head, node)
            return
        self.head = node
        self.tail = node

    def set_tail(self, node: Node):
        if self.tail:
            self.insert_after(self.tail, node)
            return
        self.set_head(node)

    def insert_before(self, node: Node, node_to_insert: Node):
        if self.head == node_to_insert and self.tail == node_to_insert:
            return
        self.remove(node_to_insert)
        node_to_insert.next = node
        node_to_insert.prev = node.prev
        if node.prev:
            node.prev.next = node_to_insert
        else:
            self.head = node_to_insert
        node.prev = node_to_insert

    def insert_after(self, node: Node, node_to_insert: Node):
        if self.head == node_to_insert and self.tail == node_to_insert:
            return
        self.remove(node_to_insert)
        node_to_insert.next = node.next
        node_to_insert.prev = node
        if node.next:
            node.next.prev = node_to_insert
        else:
            self.tail = node_to_insert
        node.next = node_to_insert

    def insert_at_position(self, position: int, node_to_insert: Node):
        if position == 1:
            self.set_head(node_to_insert)
            return
        node = self.head
        cur_position = 1
        while cur_position != position:
            node = node.next
            cur_position += 1
        if node:
            self.insert_before(node, node_to_insert)
        else:
            self.set_tail(node_to_insert)

    def remove_nodes_with_value(self, value: int):
        node = self.head
        while node:
            next_node = node.next
            if node.value == value:
                self.remove(node)
            node = next_node

    def remove(self, node: Node):
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev
        self.remove_bindings(node)

    def contains_node_with_value(self, value: int):
        node = self.head
        while node and node.value != value:
            node = node.next
        return node is not None

    def remove_bindings(self, node: Node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = None
        node.prev = None
