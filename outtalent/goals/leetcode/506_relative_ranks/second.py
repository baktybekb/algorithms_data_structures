# # https://leetcode.com/problems/relative-ranks/description/

from typing import List


# O(nlog(n)) time | O(n) space
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pairs = [(score[i], i) for i in range(len(score))]
        pairs.sort(key=lambda x: x[0], reverse=True)
        medals = ('Gold Medal', 'Silver Medal', 'Bronze Medal')

        rank_idx = 0
        ranks = [0] * len(score)
        for score, index in pairs:
            if rank_idx < 3:
                ranks[index] = medals[rank_idx]
            else:
                ranks[index] = f'{rank_idx + 1}'
            rank_idx += 1
        return ranks
