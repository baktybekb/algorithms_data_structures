# https://www.algoexpert.io/questions/dijkstra's-algorithm

# O((V + E) * log(V)) time | O(V) space
def dijkstrasAlgorithm(start, edges):
    distances = [-1] * len(edges)
    visited = set()
    heap = Heap([(0, start)], min_heap)
    while len(visited) < len(edges):
        if heap.is_empty():
            break
        dist, vertex = heap.remove()
        if vertex in visited:
            continue
        visited.add(vertex)
        distances[vertex] = dist
        for nei, distance in edges[vertex]:
            if nei in visited:
                continue
            heap.insert((dist + distance, nei))
    return distances


def min_heap(a, b):
    return a < b

class Heap:
    def __init__(self, array, func):
        self.func = func
        self.heap = self.build(array)

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def build(self, array):
        idx = (len(array) - 2) // 2
        for i in reversed(range(idx + 1)):
            self.sift_down(i, array)
        return array

    def sift_down(self, current_idx, array):
        child_one_idx = current_idx * 2 + 1
        end_idx = len(array) - 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and self.func(array[child_two_idx][0], array[child_one_idx][0]):
                swap_idx = child_two_idx
            else:
                swap_idx = child_one_idx
            if self.func(array[swap_idx][0], array[current_idx][0]):
                self.swap(swap_idx, current_idx, array)
                current_idx = swap_idx
                child_one_idx = current_idx * 2 + 1
            else:
                break

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value = self.heap.pop()
        self.sift_down(0, self.heap)
        return value

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, current_idx):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and self.func(self.heap[current_idx][0], self.heap[parent_idx][0]):
            self.swap(parent_idx, current_idx, self.heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]
