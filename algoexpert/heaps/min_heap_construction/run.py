# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for idx in reversed(range(first_parent_idx + 1)):
            self.siftDown(idx, len(array) - 1, array)
        return array

    def siftDown(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if heap[idx_to_swap] < heap[current_idx]:
                self.swap(heap, current_idx, idx_to_swap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                break

    def siftUp(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and heap[parent_idx] > heap[current_idx]:
            self.swap(heap, current_idx, parent_idx)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(self.heap, 0, len(self.heap) - 1)
        value = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return value

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]
