"""
Problem:
    Queue with two stacks. Implement a queue with two stacks so that each queue operations takes a constant amortized
    number of stack operations.

    operations: enqueue(), deque(), peek(), is_empty()
"""

import unittest


class QueueWithTwoStacks:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, value):
        self.instack.append(value)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop() if self.outstack else None

    def is_empty(self):
        return len(self.instack) == len(self.outstack) == 0

    def peek(self):
        if self.is_empty():
            return 'Queue is empty'
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]


class TestClass(unittest.TestCase):
    def test_func(self):
        queue = QueueWithTwoStacks()
        data = [3, 0, 2, 5]
        for num in data:
            queue.enqueue(num)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 0)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), None)
