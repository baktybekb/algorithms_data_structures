"""Stack"""
from data_structures.dynamic_array.ds import DynamicArray


class Stack:
    def __init__(self):
        self.data = DynamicArray()

    def __len__(self):
        return len(self.data)

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError('stack is empty')
        value = self.data.pop()
        return value

    def is_empty(self):
        return len(self.data) == 0
