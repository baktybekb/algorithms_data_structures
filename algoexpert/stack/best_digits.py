# O(n) time | O(n) space
def bestDigits(number, numDigits):
    stack = []
    for digit in number:
        while stack and numDigits > 0 and stack[-1] <= digit:
            stack.pop()
            numDigits -= 1
        stack.append(digit)
    while numDigits > 0:  # number == 321 --> all digits in a descending order
        stack.pop()
        numDigits -= 1
    return ''.join(stack)


if __name__ == '__main__':
    res = bestDigits(number='462839', numDigits=2)
    assert res == '6839'

