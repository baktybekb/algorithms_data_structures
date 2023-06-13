def mergeSortedArrays(arrays):
    items, result = [], []
    for i in range(len(arrays)):
        items.append({'array_idx': i, 'num_idx': 0, 'num': arrays[i][0]})
    heap = MinHeap(items)
    while not heap.is_empty():
        item = heap.remove()
        result.append(item['num'])
        array_idx = item['array_idx']
        num = item['num']
        num_idx = item['num_idx']
        if num_idx + 1 >= len(arrays[array_idx]):
            continue
        heap.insert(
            {'array_idx': array_idx, 'num_idx': num_idx + 1, 'num': arrays[array_idx][num_idx + 1]}
        )
    return result


class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    # O(n) time, because we us sift_down() --> starting from the bottom parents
    # O(nlog(n)), when we use sift_up() for building --> starting from the top
    def build_heap(self, array):
        last_parent_idx = (len(array) - 2) // 2
        for idx in reversed(range(last_parent_idx + 1)):
            self.sift_down(idx, len(array) - 1, array)
        return array

    def sift_up(self, current_idx, array):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and array[current_idx]['num'] < array[parent_idx]['num']:
            self.swap(array, parent_idx, current_idx)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def remove(self):
        self.swap(self.heap, 0, len(self.heap) - 1)
        value_to_remove = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value_to_remove

    def sift_down(self, current_idx, end_idx, array):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and array[child_two_idx]['num'] < array[child_one_idx]['num']:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if array[idx_to_swap]['num'] < array[current_idx]['num']:
                self.swap(array, idx_to_swap, current_idx)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                break

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]
