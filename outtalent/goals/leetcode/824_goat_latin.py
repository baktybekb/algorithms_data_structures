# https://leetcode.com/problems/goat-latin/description/

# O(n) time | O(n) space
class Solution:
    def toGoatLatin(self, sentence: str):
        array = []
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l, last_idx = 0, len(sentence) - 1
        count = 1
        for r in range(len(sentence)):
            if sentence[r] != ' ' and r < last_idx:
                continue
            start, end = l, r + (0 if r == last_idx else -1)
            if sentence[start] in vowels:
                array.append(sentence[start:end + 1])
            else:
                array.append(sentence[start + 1:end + 1])
                array.append(sentence[start])
            array.append('ma')
            array.append('a' * count)
            count += 1
            l = r + 1
            if r < last_idx:
                array.append(' ')
        return ''.join(array)


if __name__ == '__main__':
    assert Solution().toGoatLatin(sentence="I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

