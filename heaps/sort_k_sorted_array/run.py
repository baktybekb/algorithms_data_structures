# O(nlog(k)) time | O(k) space, where k ~ length of min heap, n - numbers in the array
def sortKSortedArray(array, k):
    index = 0
    heap = MinHeap(array[:k + 1])
    while heap.length > 0:
        array[index] = heap.remove()
        index += 1
        if index + k < len(array):
            heap.insert(array[index + k])
    return array


class MinHeap:
    def __init__(self, array, ):
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
    nums = [3, 2, 1, 5, 4, 7, 6, 5]
    res = sortKSortedArray(nums, k=3)
    print(nums)  # [1, 2, 3, 4, 5, 5, 6, 7]
