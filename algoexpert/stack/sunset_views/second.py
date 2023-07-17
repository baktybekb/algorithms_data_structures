# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    stack = []
    idx = len(buildings) - 1 if direction == 'WEST' else 0
    step = -1 if direction == 'WEST' else 1
    while 0 <= idx < len(buildings):
        height = buildings[idx]
        while stack and buildings[stack[-1]] <= height:
            stack.pop()
        stack.append(idx)
        idx += step
    if direction == 'EAST':
        return stack
    l, r = 0, len(stack) - 1
    while l <= r:
        swap(stack, l, r)
        l += 1
        r -= 1
    return stack


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    res = sunsetViews(buildings=[3, 5, 4, 4, 3, 1, 3, 2], direction='EAST')
    assert res == [1, 3, 6, 7]

    res = sunsetViews(buildings=[3, 5, 4, 4, 3, 1, 3, 2], direction='WEST')
    assert res == [0, 1]
