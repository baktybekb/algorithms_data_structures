# O(n) time | O(n) space
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.characterReplacement(s="AABABBA", k=1) == 4
