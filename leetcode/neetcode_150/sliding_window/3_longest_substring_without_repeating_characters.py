# O(n) time | O(n) space
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = res = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.lengthOfLongestSubstring(s="abcabcbb") == 3
    assert sol.lengthOfLongestSubstring(s="pwwkew") == 3
