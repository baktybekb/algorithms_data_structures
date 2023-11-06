# https://www.algoexpert.io/questions/phone-number-mnemonics

# O(4^n * n) time | O(4^n * n) space
def phoneNumberMnemonics(phoneNumber):
    res, subset = [], []
    number_map = {
        '0': '0',
        '1': '1',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def helper(i):
        if i == len(phoneNumber):
            res.append(''.join(subset))
            return
        options = number_map[phoneNumber[i]]
        for option in options:
            subset.append(option)
            helper(i + 1)
            subset.pop()

    helper(0)
    return res

