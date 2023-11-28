from typing import List


# # O(m * m) time | O(m) space
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         prefix = []
#         for i in range(len(strs[0])):
#             for s in strs:
#                 if i == len(s) or s[i] != strs[0][i]:
#                     return ''.join(prefix)
#             prefix.append(strs[0][i])
#         return ''.join(prefix) if prefix else ''


# O(m * m) time | O(m) space
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = list(strs[0])
        for i in range(1, len(strs)):
            while len(strs[i]) < len(prefix):
                prefix.pop()
            for j in reversed(range(len(prefix))):
                if strs[i][j] != prefix[j]:
                    prefix.pop()
        return ''.join(prefix)


if __name__ == '__main__':
    res = Solution().longestCommonPrefix(["flower", "flow", "flight"])
    print(res)


