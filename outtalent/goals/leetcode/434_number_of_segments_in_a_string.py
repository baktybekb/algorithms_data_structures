# https://leetcode.com/problems/number-of-segments-in-a-string/description/

# O(n) time | O(1) space
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                count += 1
        return count


if __name__ == '__main__':
    assert Solution().countSegments(" Hello, my name is John ") == 5
