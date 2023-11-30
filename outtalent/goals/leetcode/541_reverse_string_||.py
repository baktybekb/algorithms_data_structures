# https://leetcode.com/problems/reverse-string-ii/description/

# O(n) time | O(n) space
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        array = list(s)
        for i in range(0, len(s), k * 2):
            l, r = i, min(i + k - 1, len(s) - 1)
            while l < r:
                array[l], array[r] = array[r], array[l]
                l += 1
                r -= 1
        return ''.join(array)


