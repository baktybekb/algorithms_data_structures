# O(n^2) time | O(n) space
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled = s + s
        if s in doubled[1:-1]:  # O(n^2) time, need to use KMP algorithm for better time complexity
            return True
        return False
