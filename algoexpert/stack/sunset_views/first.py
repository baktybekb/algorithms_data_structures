# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    range_ = range(len(buildings))
    iterator = range_ if direction == "WEST" else reversed(range_)
    running_max = 0
    array = []
    for i in iterator:
        if buildings[i] <= running_max:
            continue
        array.append(i)
        running_max = buildings[i]
    if direction == 'WEST':
        return array
    return reverse(array)


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
