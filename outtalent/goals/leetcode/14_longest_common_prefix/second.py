# https://leetcode.com/problems/longest-common-prefix/description/

from typing import List


# O(n * s) time | O(s) space, n - len(strs), s - length of 1st string
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return ''.join(prefix)
            prefix.append(strs[0][i])
        return ''.join(prefix)
