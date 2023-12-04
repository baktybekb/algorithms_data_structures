# https://leetcode.com/problems/robot-return-to-origin/description/

# O(n) time | O(1) space
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for char in moves:
            if char == 'U':
                y += 1
            elif char == 'D':
                y -= 1
            elif char == 'L':
                x -= 1
            else:
                x += 1
        return x == y == 0
