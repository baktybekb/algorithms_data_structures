# O(n) time | O(k) space
class KthLargest:
    def __init__(self, k, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
        self.k = k
        self.udpate_heap_size()

    def buildHeap(self, array):
        idx = (len(array) - 1) // 2
        for i in reversed(range(idx + 1)):
            self.siftDown(i, array)
        return array

    def siftDown(self, current_idx, array):
        child_one_idx = current_idx * 2 + 1
        end_idx = len(array) - 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and array[child_two_idx] < array[child_one_idx]:
                swap_idx = child_two_idx
            else:
                swap_idx = child_one_idx
            if array[swap_idx] < array[current_idx]:
                self.swap(swap_idx, current_idx, array)
                current_idx = swap_idx
                child_one_idx = current_idx * 2 + 1
            else:
                break

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

    def siftUp(self, current_idx):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and self.heap[parent_idx] > self.heap[current_idx]:
            self.swap(current_idx, parent_idx, self.heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value = self.heap.pop()
        self.siftDown(0, self.heap)
        return value

    def add(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)
        self.udpate_heap_size()
        return self.heap[0]

    def udpate_heap_size(self):
        while len(self.heap) > self.k:
            self.remove()
