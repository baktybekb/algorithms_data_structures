# https://www.algoexpert.io/questions/permutations

# O(n! * n) time | O(n! * n) space
def getPermutations(array):
    res = []

    def helper(i):
        if i == len(array) - 1:
            res.append(array.copy())
            return
        for j in range(i, len(array)):
            swap(i, j, array)
            helper(i + 1)
            swap(i, j, array)

    helper(0)
    return res


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
