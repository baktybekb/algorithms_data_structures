# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    prev = current = 0
    for i in range(len(array)):
        temp = current
        current = max(prev + array[i], current)
        prev = temp
    return current
