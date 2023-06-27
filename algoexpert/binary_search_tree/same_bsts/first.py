# O(n^2) time | O(n^2) space
def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    if len(arrayOne) != len(arrayTwo):
        return False
    if arrayOne[0] != arrayTwo[0]:
        return False
    left_one = get_smaller(arrayOne)
    left_two = get_smaller(arrayTwo)
    right_one = get_greater(arrayOne)
    right_two = get_greater(arrayTwo)
    left_same = sameBsts(left_one, left_two)
    right_same = sameBsts(right_one, right_two)
    return left_same and right_same


def get_smaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller


def get_greater(array):
    greater = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            greater.append(array[i])
    return greater
