# O(n) time | O(n) space
def balancedBrackets(string):
    opening = '({['
    mapper = {')': '(', '}': '{', ']': '['}
    stack = []
    for bracket in string:
        if bracket in opening:
            stack.append(bracket)
        elif bracket in mapper:
            if not stack or stack[-1] != mapper[bracket]:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == '__main__':
    assert balancedBrackets('(agwgg)([])') is True
    assert balancedBrackets('()([])]') is False

