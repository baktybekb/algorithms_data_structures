# https://leetcode.com/problems/roman-to-integer/description/

# O(n) time | O(1) space
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        number = 0
        for i in range(len(s) - 1):
            current_value = symbol_map[s[i]]
            next_value = symbol_map[s[i + 1]]
            if current_value < next_value:
                number += -current_value
            else:
                number += current_value
        return number + symbol_map[s[-1]]

