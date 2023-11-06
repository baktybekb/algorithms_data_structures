from typing import List


# O(n! * n) time | O(n^2) space
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if not self.is_pali(i, j, s):
                    continue
                part.append(s[i:j + 1])
                dfs(j + 1)
                part.pop()

        dfs(0)
        return res

    def is_pali(self, i, j, string):
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True
