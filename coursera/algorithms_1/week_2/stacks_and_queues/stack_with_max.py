import unittest

"""
Problem:
    Stack with max. Create a data structure that efficiently supports the stack operations (push and pop)
    and also a return-the-maximum operation. Assume the elements are real numbers so that you can compare them.
"""


class MinMaxStack:
    def __init__(self):
        self.min_max_stack = []
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        value_to_pop = self.stack.pop()
        self.min_max_stack.pop()
        return value_to_pop

    def push(self, number):
        if not self.stack:
            self.stack.append(number)
            self.min_max_stack.append((number, number))
            return
        self.stack.append(number)
        cur_min, cur_max = self.min_max_stack[-1]
        self.min_max_stack.append((min(cur_min, number), max(cur_max, number)))

    def get_min(self):
        return self.min_max_stack[-1][0]

    def get_max(self):
        return self.min_max_stack[-1][1]


class TestClass(unittest.TestCase):
    def test_func(self):
        stack = MinMaxStack()
        stack.push(5)
        self.assertEqual(stack.get_min(), 5)
        self.assertEqual(stack.get_max(), 5)
        stack.push(2)
        self.assertEqual(stack.get_min(), 2)
        self.assertEqual(stack.get_max(), 5)
        stack.push(50)
        self.assertEqual(stack.get_min(), 2)
        self.assertEqual(stack.get_max(), 50)
        stack.pop()
        self.assertEqual(stack.get_min(), 2)
        self.assertEqual(stack.get_max(), 5)


