# https://leetcode.com/problems/word-ladder/description/

from collections import deque
from typing import List


# O(n * m^2) time | O(n * m^2) space
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns = {}
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '#' + word[i + 1:]
                if pattern not in patterns:
                    patterns[pattern] = []
                patterns[pattern].append(word)
        visited, sequence = {beginWord}, 1
        queue = deque([beginWord])
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return sequence
                for j in range(len(word)):
                    pattern = word[:j] + '#' + word[j + 1:]
                    for neighbor in patterns[pattern]:
                        if neighbor in visited:
                            continue
                        visited.add(neighbor)
                        queue.append(neighbor)
            sequence += 1
        return 0
