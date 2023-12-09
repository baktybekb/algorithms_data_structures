from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        pairs = [(arr[i], i) for i in range(len(arr))]
        pairs.sort(key=lambda x: x[0])
        ranks = [0] * len(arr)
        rank, prev = 1, None
        for val, index in pairs:  # non-decreasing order
            if prev is not None and prev < val:
                rank += 1
            ranks[index] = rank
            prev = val
        return ranks

