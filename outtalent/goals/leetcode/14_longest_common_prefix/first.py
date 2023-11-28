# https://leetcode.com/problems/longest-common-prefix/description/

from typing import List


# O(n * s) time | O(s) space, n - len(strs), s - length of 1st string
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = list(strs[0])
        for i in range(1, len(strs)):
            while len(strs[i]) < len(prefix):
                prefix.pop()
            for j in reversed(range(len(prefix))):
                if strs[i][j] == prefix[j]:
                    continue
                for k in range(j, len(prefix)):
                    prefix.pop()
        return ''.join(prefix)


