"""Stack"""


class Node:
    __slots__ = 'value', 'next'

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def push(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('stack is empty')
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value

    def is_empty(self):
        return self.head is None
