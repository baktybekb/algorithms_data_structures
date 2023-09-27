# https://www.algoexpert.io/questions/largest-range

# O(n) time | O(n) space
def largestRange(array):
    array_set = set(array)
    res = [0, 0]
    for num in array:
        if num - 1 in array_set:
            continue
        i = 1
        while num + i in array_set:
            i += 1
        if res[1] - res[0] < i:
            res = [num, num + i - 1]
    return res


if __name__ == '__main__':
    assert largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]) == [0, 7]
