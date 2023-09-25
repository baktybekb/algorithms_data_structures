# https://www.algoexpert.io/questions/array-of-products

# O(n) time | O(n) space
def arrayOfProducts(array):
    res = [1] * len(array)
    multiplier = 1
    for i in range(len(array)):
        res[i] *= multiplier
        multiplier *= array[i]
    multiplier = 1
    for i in reversed(range(len(array))):
        res[i] *= multiplier
        multiplier *= array[i]
    return res

