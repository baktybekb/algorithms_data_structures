# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.left = Heap([], max_heap_func)
        self.right = Heap([], min_heap_func)

    def insert(self, number):
        if self.left.length == 0 or number < self.left.peek():
            self.left.insert(number)
        else:
            self.right.insert(number)
        self.rebalance()
        self.update_median()

    def update_median(self):
        if self.left.length == self.right.length:
            self.median = (self.left.peek() + self.right.peek()) / 2
        elif self.left.length > self.right.length:
            self.median = self.left.peek()
        else:
            self.median = self.right.peek()

    def rebalance(self):
        if abs(self.left.length - self.right.length) <= 1:
            return
        if self.left.length > self.right.length:
            self.right.insert(self.left.remove())
            return
        self.left.insert(self.right.remove())

    def getMedian(self):
        return self.median


class Heap:
    def __init__(self, array, func):
        self.heap = self.build_heap(array)
        self.func = func
        self.length = len(self.heap)

    def build_heap(self, array):
        last_parent_idx = (len(array) - 2) // 2
        for idx in reversed(range(last_parent_idx + 1)):
            self.sift_down(idx, len(array) - 1, array)
        return array

    def sift_down(self, current_idx, end_idx, array):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else - 1
            if child_two_idx != -1 and self.func(array[child_two_idx], array[child_one_idx]):
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if self.func(array[idx_to_swap], array[current_idx]):
                self.swap(array, idx_to_swap, current_idx)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                break

    def sift_up(self, current_idx, array):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and self.func(array[current_idx], array[parent_idx]):
            self.swap(array, current_idx, parent_idx)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)
        self.length += 1

    def remove(self):
        self.swap(self.heap, 0, len(self.heap) - 1)
        value_to_remove = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        self.length -= 1
        return value_to_remove

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]


def max_heap_func(a, b):
    return a > b


def min_heap_func(a, b):
    return a < b

