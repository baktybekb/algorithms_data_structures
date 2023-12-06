# https://leetcode.com/problems/detect-capital/description/


# O(n) time | O(1) space
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all(word[i].islower() for i in range(1, len(word))):
            return True
        return all(char.isupper() for char in word)


