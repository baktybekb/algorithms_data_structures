# https://leetcode.com/problems/last-stone-weight/description/

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = Heap(stones, max_heap)
        while len(heap) >= 2:
            one = heap.remove()
            two = heap.remove()
            if one == two:
                continue
            heap.insert(one - two)
        return heap.peek() if len(heap) == 1 else 0


class Heap:
    def __init__(self, array, func):
        self.func = func
        self.heap = self.build(array)

    def __len__(self):
        return len(self.heap)

    # O(n) time | O(1) space
    def build(self, array):
        parent_idx = (len(array) - 2) // 2
        for i in reversed(range(parent_idx + 1)):
            self.sift_down(i, array)
        return array

    def sift_down(self, current_idx, array):
        child_one_idx = current_idx * 2 + 1
        end_idx = len(array) - 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else - 1
            if child_two_idx != -1 and self.func(array[child_one_idx], array[child_two_idx]):
                swap_idx = child_two_idx
            else:
                swap_idx = child_one_idx
            if self.func(array[current_idx], array[swap_idx]):
                self.swap(swap_idx, current_idx, array)
                current_idx = swap_idx
                child_one_idx = current_idx * 2 + 1
            else:
                break

    def peek(self):
        return self.heap[0]

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

    # O(log(n)) time | O(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value = self.heap.pop()
        self.sift_down(0, self.heap)
        return value

    # O(log(n)) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, current_idx):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and self.func(self.heap[parent_idx], self.heap[current_idx]):
            self.swap(current_idx, parent_idx, self.heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2


def max_heap(a, b):
    return a < b


def min_heap(a, b):
    return a > b
