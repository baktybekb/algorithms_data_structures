from typing import List


# O(n * m) time | O(n * m) space
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = Heap([(grid[0][0], 0, 0)], min_heap)
        visited = {(0, 0)}
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        while not heap.is_empty():
            height, cur_row, cur_col = heap.remove()
            if cur_row == rows - 1 and cur_col == cols - 1:
                return height
            for r, c in directions:
                row, col = cur_row + r, cur_col + c
                if not 0 <= row < rows or not 0 <= col < cols:
                    continue
                if (row, col) in visited:
                    continue
                visited.add((row, col))
                heap.insert((max(height, grid[row][col]), row, col))


def min_heap(a, b):
    return a < b


class Heap:
    def __init__(self, array, func):
        self.func = func
        self.heap = self.build(array)

    def is_empty(self):
        return len(self.heap) == 0

    def build(self, array):
        last_parent_idx = (len(array) - 2) // 2
        for i in reversed(range(last_parent_idx + 1)):
            self.sift_down(i, array)
        return array

    def sift_down(self, current_idx, array):
        child_idx_1 = current_idx * 2 + 1
        end_idx = len(array) - 1
        while child_idx_1 <= end_idx:
            child_idx_2 = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_idx_2 != -1 and self.func(array[child_idx_2][0], array[child_idx_1][0]):
                swap_idx = child_idx_2
            else:
                swap_idx = child_idx_1
            if self.func(array[swap_idx][0], array[current_idx][0]):
                self.swap(swap_idx, current_idx, array)
                current_idx = swap_idx
                child_idx_1 = current_idx * 2 + 1
            else:
                break

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, current_idx):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and self.func(self.heap[current_idx][0], self.heap[parent_idx][0]):
            self.swap(current_idx, parent_idx, self.heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def peak(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value = self.heap.pop()
        self.sift_down(0, self.heap)
        return value

