from typing import List


# O(n * klogk) time | O(n) space
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for val in strs:
            sorted_val = ''.join(sorted(val))
            if sorted_val in mapper:
                mapper[sorted_val].append(val)
            else:
                mapper[sorted_val] = [val]
        return [i for i in mapper.values()]
