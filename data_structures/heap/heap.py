def max_heap_func(a, b):
    return a > b


def min_heap_func(a, b):
    return a < b


class Heap:
    def __init__(self, array, func):
        self.func = func
        self.heap = self.build(array)

    def build(self, array):
        last_parent_idx = (len(array) - 2) // 2
        for idx in reversed(range(last_parent_idx + 1)):
            self.sift_down(idx, array)
        return array

    # O(log(n)) time | O(1) space
    def sift_up(self, current_idx):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and self.func(self.heap[current_idx], self.heap[parent_idx]):
            self.swap(self.heap, parent_idx, current_idx)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    # O(log(n)) time | O(1) space
    def sift_down(self, current_idx, heap):
        end_idx = len(heap) - 1
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and self.func(heap[child_two_idx], heap[child_one_idx]):
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if self.func(heap[idx_to_swap], heap[current_idx]):
                self.swap(heap, current_idx, idx_to_swap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                break

    def remove(self):
        self.swap(self.heap, 0, len(self.heap) - 1)
        value = self.heap.pop()
        self.sift_down(0, self.heap)
        return value

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]

