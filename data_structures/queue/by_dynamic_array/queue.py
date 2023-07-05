"""Queue"""
from data_structures.dynamic_array.ds import DynamicArray


class Queue:
    def __init__(self):
        self.array = DynamicArray()
        self.head_index = 0

    def enqueue(self, value):
        self.array.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        value = self.array[self.head_index]
        self.head_index += 1
        if self.head_index > len(self.array) // 2:
            self.array = self.array.get_from_index(self.head_index)
            self.head_index = 0
        return value

    def is_empty(self):
        return self.head_index == len(self.array)

    def peek(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        return self.array[self.head_index]

    def __len__(self):
        return len(self.array) - self.head_index
