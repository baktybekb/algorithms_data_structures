# https://leetcode.com/problems/relative-ranks/description/

from typing import List


# O(nlog(n)) time | O(n) space
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pairs = [(score[i], i) for i in range(len(score))]
        heap = Heap(pairs, max_heap)
        ranks = [0] * len(score)
        medals = ("Gold Medal", "Silver Medal", "Bronze Medal")
        rank_idx = 0
        while not heap.is_empty():
            value, index = heap.remove()
            if rank_idx < 3:
                ranks[index] = medals[rank_idx]
            else:
                ranks[index] = f'{rank_idx + 1}'
            rank_idx += 1
        return ranks


def max_heap(a, b):
    return a > b


class Heap:
    def __init__(self, array, func):
        self.func = func
        self.heap = self.build(array)

    def is_empty(self):
        return len(self.heap) == 0

    def build(self, array):
        parent_idx = (len(array) - 2) // 2
        end_idx = len(array) - 1
        for i in reversed(range(parent_idx + 1)):
            self.sift_down(i, end_idx, array)
        return array

    def sift_down(self, index, end_idx, array):
        index_one = index * 2 + 1
        while index_one <= end_idx:
            index_two = index * 2 + 2 if index * 2 + 2 <= end_idx else -1
            if index_two != -1 and self.func(array[index_two][0], array[index_one][0]):
                swap_idx = index_two
            else:
                swap_idx = index_one
            if self.func(array[swap_idx][0], array[index][0]):
                self.swap(swap_idx, index, array)
                index = swap_idx
                index_one = index * 2 + 1
            else:
                break

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value


