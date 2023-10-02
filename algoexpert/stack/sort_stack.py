# https://www.algoexpert.io/questions/sort-stack

# O(n ^ 2) time | O(n) space
def sortStack(stack):
    if not stack:
        return stack
    val = stack.pop()
    sortStack(stack)
    insert(stack, val)
    return stack


def insert(stack, val):
    if not stack or stack[-1] <= val:
        stack.append(val)
        return
    last = stack.pop()
    insert(stack, val)
    stack.append(last)


if __name__ == '__main__':
    assert sortStack([-5, 2, -2, 4, 3, 1]) == [-5, -2, 1, 2, 3, 4]

