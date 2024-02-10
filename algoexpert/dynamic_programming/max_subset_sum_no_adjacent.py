# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0
    sum_array = [0] * len(array)
    for i in range(len(array)):
        prev = 0 if i - 2 < 0 else sum_array[i - 2]
        current = 0 if i - 1 < 0 else sum_array[i - 1]
        sum_array[i] = max(current, prev + array[i])
    return sum_array[-1]


if __name__ == '__main__':
    array = [75, 105, 120, 75, 90, 135]
    assert maxSubsetSumNoAdjacent(array) == 330
