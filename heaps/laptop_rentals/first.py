# worse time complexity than solution 2, but better space complexity
# O(nlog(n)) time | O(n) space
def laptopRentals(times: list):
    if not times:
        return 0
    times.sort(key=lambda x: x[0])
    heap = MinHeap([times[0][1]])
    for i in range(1, len(times)):
        start, end = times[i]
        if start >= heap.peek():
            heap.remove()
        heap.insert(end)
    return heap.length


class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)
        self.length = len(self.heap)

    # O(n) time, because we us sift_down() --> starting from the bottom parents
    # O(nlog(n)), when we use sift_up() for building --> starting from the top
    def build_heap(self, array):
        last_parent_idx = (len(array) - 2) // 2
        for idx in reversed(range(last_parent_idx + 1)):
            self.sift_down(idx, len(array) - 1, array)
        return array

    def sift_up(self, current_idx, array):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and array[current_idx] < array[parent_idx]:
            self.swap(array, parent_idx, current_idx)
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

    def sift_down(self, current_idx, end_idx, array):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and array[child_two_idx] < array[child_one_idx]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if array[idx_to_swap] < array[current_idx]:
                self.swap(array, idx_to_swap, current_idx)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                break

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    data = [
        [0, 2],
        [1, 4],
        [4, 6],
        [0, 4],
        [7, 8],
        [9, 11],
        [3, 10]
    ]
    laptopRentals(data)
