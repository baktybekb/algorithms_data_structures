# https://www.algoexpert.io/questions/reversePolishNotation

# O(n) time | O(n) space
def reversePolishNotation(tokens):
    stack = []
    for token in tokens:
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            val = stack.pop()
            stack.append(stack.pop() - val)
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            val = stack.pop()
            stack.append(int(stack.pop() / val))
        else:
            stack.append(int(token))
    return stack[-1]


if __name__ == '__main__':
    assert reversePolishNotation(["3", "2", "+", "7", "*"]) == 35
