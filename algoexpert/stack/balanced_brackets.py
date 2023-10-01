# https://www.algoexpert.io/questions/balanced-brackets

# O(n) time | O(n) space
def balancedBrackets(string):
    stack = []
    mapper = {')': '(', '}': '{', ']': '['}
    opened = {'(', '{', '['}
    for bracket in string:
        if bracket in opened:
            stack.append(bracket)
            continue
        if bracket not in mapper:
            continue
        if not stack:
            return False
        if mapper[bracket] != stack[-1]:
            return False
        stack.pop()
    return False if stack else True
