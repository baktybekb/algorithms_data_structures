# https://leetcode.com/problems/student-attendance-record-i/description/

# O(n) time | O(1) space
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        for i in range(len(s)):
            if s[i] == 'A':
                absent += 1
                if absent == 2:
                    return False
            elif s[i] == 'L':
                index = i
                while index < len(s) and s[index] == 'L':
                    index += 1
                    if index - i == 3:
                        return False
            else:
                continue
        return True
