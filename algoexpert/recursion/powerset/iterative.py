# https://www.algoexpert.io/questions/powerset

# O(2^n * n) time | O(n^2 * n) space
def powerset(array):
    subsets = [[]]
    for val in array:
        for subset in subsets:
            subsets.append(subset + [val])
    return subsets
