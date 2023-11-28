# https://leetcode.com/problems/isomorphic-strings/description/

# O(s) time | O(s + t) space
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map, t_map = {}, {}
        for i in range(len(s)):
            if s[i] in s_map and s_map[s[i]] != t[i]:
                return False
            s_map[s[i]] = t[i]

            if t[i] in t_map and t_map[t[i]] != s[i]:
                return False
            t_map[t[i]] = s[i]
        return True
