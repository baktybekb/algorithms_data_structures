# https://www.algoexpert.io/questions/three-number-sort

# O(n) time | O(1) space
def threeNumberSort(array, order):
    count_map = {val: 0 for val in order}
    for val in array:
        count_map[val] += 1
    idx = 0
    for val, quantity in count_map.items():
        for i in range(quantity):
            array[idx] = val
            idx += 1
    return array
