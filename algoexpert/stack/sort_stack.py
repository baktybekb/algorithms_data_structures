# O(n^2) time | O(n) space
def sortStack(stack):
    if not stack:
        return stack
    top = stack.pop()
    sortStack(stack)
    insert(stack, top)
    return stack


def insert(stack: list, value):
    if not stack or stack[-1] < value:
        stack.append(value)
    else:
        top = stack.pop()
        insert(stack, value)
        stack.append(top)


if __name__ == '__main__':
    res = sortStack([-5, 2, -2, 4, 3, 1])
    print(res)
