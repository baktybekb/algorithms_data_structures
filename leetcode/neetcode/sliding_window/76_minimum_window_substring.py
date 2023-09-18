# O(n) time | O(n) space
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '' or len(s) < len(t):
            return ''
        count_t, window = {}, {}
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
        have, need = 0, len(count_t)
        res_l, res_r, res_len = 0, 0, float('inf')
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)
            if char in count_t and window[char] == count_t[char]:
                have += 1
            while have == need:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res_l, res_r = l, r
                l_char = s[l]
                window[l_char] -= 1
                if l_char in count_t and window[l_char] < count_t[l_char]:
                    have -= 1
                l += 1
        return s[res_l:res_r + 1] if res_len != float('inf') else ''


if __name__ == '__main__':
    sol = Solution()
    assert sol.minWindow(s="ADOBECODEBANC", t="ABC") == 'BANC'
    assert sol.minWindow(s="a", t="aa") == ''
    assert sol.minWindow(s="a", t="a") == 'a'
    assert sol.minWindow(s="a", t="b") == ''
    assert sol.minWindow(s="ab", t="a") == 'a'
