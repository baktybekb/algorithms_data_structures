# O((v + e) * log(v)) time | O(v) space
def dijkstrasAlgorithm(start, edges):
    vertices_count = len(edges)
    min_distances = [float('inf') for i in range(vertices_count)]
    min_distances[start] = 0

    min_heap = Minheap([(i, float('inf')) for i in range(vertices_count)])
    min_heap.update(start, 0)

    while not min_heap.is_empty():
        vertex, distance = min_heap.remove()
        if distance == float('inf'):
            break
        for edge in edges[vertex]:
            destination, distance_to_dest = edge
            current_distance = min_distances[destination]
            new_path_dist = distance + distance_to_dest
            if new_path_dist >= current_distance:
                continue
            min_distances[destination] = new_path_dist
            min_heap.update(destination, new_path_dist)
    return list(map(lambda x: -1 if x == float('inf') else x, min_distances))


class Minheap:
    def __init__(self, array):
        self.vertex_map = {i: i for i in range(len(array))}
        self.heap = self.build_heap(array)

    def is_empty(self):
        return len(self.heap) == 0

    def build_heap(self, array):
        parent_idx = (len(array) - 2) // 2
        for idx in reversed(range(parent_idx + 1)):
            self.sift_down(array, idx)
        return array

    def sift_down(self, array, current_idx):
        end_idx = len(array) - 1
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and array[child_two_idx][1] < array[child_one_idx][1]:
                idx_two_swap = child_two_idx
            else:
                idx_two_swap = child_one_idx
            if array[idx_two_swap][1] < array[current_idx][1]:
                self.swap(array, idx_two_swap, current_idx)
                current_idx = idx_two_swap
                child_one_idx = current_idx * 2 + 1
            else:
                break

    def sift_up(self, current_idx):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and self.heap[current_idx][1] < self.heap[parent_idx][1]:
            self.swap(self.heap, current_idx, parent_idx)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def swap(self, array, i, j):
        self.vertex_map[array[i][0]] = j
        self.vertex_map[array[j][0]] = i
        array[i], array[j] = array[j], array[i]

    def remove(self):
        self.swap(self.heap, 0, len(self.heap) - 1)
        vertex, distance = self.heap.pop()
        self.vertex_map.pop(vertex)
        self.sift_down(self.heap, 0)
        return vertex, distance

    def update(self, vertex, distance):
        idx = self.vertex_map[vertex]
        self.heap[idx] = (vertex, distance)
        self.sift_up(idx)


if __name__ == '__main__':
    assert dijkstrasAlgorithm(
        start=0,
        edges=[
            [[1, 7]],
            [[2, 6], [3, 20], [4, 3]],
            [[3, 14]],
            [[4, 2]],
            [],
            []
        ]
    ) == [0, 7, 13, 27, 10, -1]

    assert dijkstrasAlgorithm(
        start=7,
        edges=[
            [[1, 1], [3, 1]],
            [[2, 1]],
            [[6, 1]],
            [[1, 3], [2, 4], [4, 2], [5, 3], [6, 5]],
            [[5, 1]],
            [[4, 1]],
            [[5, 2]],
            [[0, 7]]
        ]
    ) == [7, 8, 9, 8, 10, 11, 10, 0]
