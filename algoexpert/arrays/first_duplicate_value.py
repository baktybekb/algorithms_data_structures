# https://www.algoexpert.io/questions/first-duplicate-value

# O(n) time | O(1) space
def firstDuplicateValue(array):
    for num in array:
        index = abs(num) - 1
        if array[index] < 0:
            return abs(num)
        array[index] *= -1
    return -1


if __name__ == '__main__':
    assert firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]) == 2
    assert firstDuplicateValue([2, 1, 5, 3, 3, 2, 4]) == 3
