# https://www.algoexpert.io/questions/product-sum

# O(n) time | O(d) space, d --> max depth of nested lists
def productSum(array, depth=1):
    total = 0
    for val in array:
        if isinstance(val, list):
            total += productSum(val, depth + 1)
        else:
            total += val
    return depth * total
