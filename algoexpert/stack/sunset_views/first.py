# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    running_max = 0
    result = []
    range_ = range(len(buildings))
    iterator = reversed(range_) if direction == 'EAST' else range_
    for i in iterator:
        if buildings[i] <= running_max:
            continue
        result.append(i)
        running_max = buildings[i]
    if direction == 'WEST':
        return result
    start, end = 0, len(result) - 1
    while start <= end:
        swap(result, start, end)
        start += 1
        end -= 1
    return result


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    res = sunsetViews(buildings=[3, 5, 4, 4, 3, 1, 3, 2], direction='EAST')
    assert res == [1, 3, 6, 7]

    res = sunsetViews(buildings=[3, 5, 4, 4, 3, 1, 3, 2], direction='WEST')
    assert res == [0, 1]
