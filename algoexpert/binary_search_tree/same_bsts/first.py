# https://www.algoexpert.io/questions/same-bsts

# O(n^2) time | O(n^2) space
def sameBsts(one, two):
    if len(one) == len(two) == 0:
        return True
    if len(one) != len(two) or one[0] != two[0]:
        return False
    left_one = get_left_tree(one, one[0])
    right_one = get_right_tree(one, one[0])

    left_two = get_left_tree(two, two[0])
    right_two = get_right_tree(two, two[0])
    return sameBsts(left_one, left_two) and sameBsts(right_one, right_two)


def get_left_tree(array, value):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < value:
            smaller.append(array[i])
    return smaller


def get_right_tree(array, value):
    greater = []
    for i in range(1, len(array)):
        if array[i] >= value:
            greater.append(array[i])
    return greater





