# O(n * log(k)) time | O(k) space
def sortKSortedArray(array, k):
    heap = Heap(array[:k + 1])
    index = 0
    while len(heap):
        array[index] = heap.remove()
        index += 1
        if index + k < len(array):
            heap.insert(array[index + k])
    return array


class Heap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        last_parent_idx = len(array) - 2 // 2
        for idx in reversed(range(last_parent_idx + 1)):
            self.siftDown(array, idx)
        return array

    def __len__(self):
        return len(self.heap)

    def siftDown(self, array, current_idx):
        end_idx = len(array) - 1
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

    def siftUp(self):
        current_idx = len(self.heap) - 1
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and self.heap[current_idx] < self.heap[parent_idx]:
            self.swap(self.heap, parent_idx, current_idx)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(self.heap, 0, len(self.heap) - 1)
        value = self.heap.pop()
        self.siftDown(self.heap, 0)
        return value

    def insert(self, value):
        self.heap.append(value)
        self.siftUp()

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 4, 7, 6, 5]
    res = sortKSortedArray(nums, k=3)
    print(nums)  # [1, 2, 3, 4, 5, 5, 6, 7]
