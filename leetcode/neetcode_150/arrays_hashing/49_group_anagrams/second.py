from typing import List


# O(n * k * 26) time | O(n * k) space
# 26 --> constant
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            count = tuple(count)
            if count in res:
                res[count].append(s)
            else:
                res[count] = [s]
        return res.values()
