# https://www.algoexpert.io/questions/best-digits

# O(n) time | O(n) space
def bestDigits(number, numDigits):
    stack = []
    count = 0
    for i in range(len(number)):
        while stack and stack[-1] <= number[i] and count < numDigits:
            stack.pop()
            count += 1
        stack.append(number[i])
    while count < numDigits:  # case when numbers are decreasing: 4321
        stack.pop()
        count += 1
    return "".join(stack)


if __name__ == '__main__':
    assert bestDigits("321", numDigits=1) == '32'
