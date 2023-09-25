# O(n) time | O(1) space
def isMonotonic(array):
    if len(array) <= 1:
        return True
    direction = None
    l, r = 0, 1
    while r < len(array):
        while r < len(array) and array[l] == array[r]:
            r += 1
        if r == len(array):
            return True
        if direction:
            cur_direct = 1 if array[l] < array[r] else -1
            if cur_direct != direction:
                return False
        else:
            direction = 1 if array[l] < array[r] else -1
        l = r
        r += 1
    return True


if __name__ == '__main__':
    assert isMonotonic(
        [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]
    ) is False
    assert isMonotonic([-1, -1, -1, -1, -1, -1, -1, -1]) is True
    assert isMonotonic([1, 2, 0]) is False
