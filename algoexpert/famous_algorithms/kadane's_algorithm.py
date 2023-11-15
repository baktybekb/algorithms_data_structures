# https://www.algoexpert.io/questions/kadane's-algorithm

# O(n) time | O(1) space
def kadanesAlgorithm(array):
    total = current = float('-inf')
    for val in array:
        current = max(current + val, val)
        total = max(total, current)
    return total

