# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    idx = 0 if direction == 'EAST' else len(buildings) - 1
    step = 1 if direction == 'EAST' else -1
    stack = []
    while 0 <= idx < len(buildings):
        while stack and buildings[stack[-1]] <= buildings[idx]:
            stack.pop()
        stack.append(idx)
        idx += step
    if direction == 'EAST':
        return stack
    return reverse(stack)


def reverse(array):
    l, r = 0, len(array) - 1
    while l <= r:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1
    return array


if __name__ == '__main__':
    res = sunsetViews(buildings=[3, 5, 4, 4, 3, 1, 3, 2], direction='EAST')
    assert res == [1, 3, 6, 7]

    res = sunsetViews(buildings=[3, 5, 4, 4, 3, 1, 3, 2], direction='WEST')
    assert res == [0, 1]
