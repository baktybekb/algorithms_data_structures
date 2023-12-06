# https://leetcode.com/problems/license-key-formatting/description/

# O(n) time | O(n) space
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        array = []
        index = len(s) % k
        if index == 0:
            index = k
        for i in range(len(s)):
            if index == i:
                array.append('-')
                index += k
            array.append(s[i])
        return ''.join(array)


