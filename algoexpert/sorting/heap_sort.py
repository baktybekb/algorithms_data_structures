# https://www.algoexpert.io/questions/heap-sort

# O(nlog(n)) time | O(1) space
def heapSort(array):
    heap = Heap(array, max_heap)
    for i in reversed(range(1, len(array))):
        heap.swap(0, i, array)
        heap.sift_down(0, i - 1, array)
    return array


def max_heap(a, b):
    return a > b


class Heap:
    def __init__(self, array, func):
        self.func = func
        self.heap = self.build(array)

    def build(self, array):
        parent_idx = (len(array) - 2) // 2
        for i in reversed(range(parent_idx + 1)):
            self.sift_down(i, len(array) - 1, array)
        return array

    def sift_down(self, current_idx, end_idx, array):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and self.func(array[child_two_idx], array[child_one_idx]):
                swap_idx = child_two_idx
            else:
                swap_idx = child_one_idx
            if self.func(array[swap_idx], array[current_idx]):
                self.swap(swap_idx, current_idx, array)
                current_idx = swap_idx
                child_one_idx = current_idx * 2 + 1
            else:
                break

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]
