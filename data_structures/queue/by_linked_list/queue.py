class Node:
    __slots__ = 'value', 'next'

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        node = Node(value)
        self.length += 1
        if self.is_empty():
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.length -= 1
        return value

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        return self.head.value

    def __len__(self):
        return self.length
