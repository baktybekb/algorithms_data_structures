# O(n) time | O(1) space
def isMonotonic(array):
    if len(array) <= 1:
        return True
    up = down = True
    for i in range(1, len(array)):
        if not up and not down:
            return False
        if array[i - 1] < array[i]:
            down = False
        elif array[i - 1] > array[i]:
            up = False
    return up or down


if __name__ == '__main__':
    assert isMonotonic(
        [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]
    ) is False
    assert isMonotonic([-1, -1, -1, -1, -1, -1, -1, -1]) is True
    assert isMonotonic([1, 2, 0]) is False
