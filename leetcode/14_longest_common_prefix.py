from typing import List


# O(k * n) time | O(k) space
# k - length of first word, n - length of strs
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = list()
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return ''.join(res)
            res.append(strs[0][i])
        return ''.join(res)
