# O(n! * n) time | O(n! * n) space
def getPermutations(array):
    result = []
    helper(0, array, result)
    return result


def helper(i, array, result):
    if i == len(array) - 1:
        result.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(i, j, array)
            helper(i + 1, array, result)
            swap(i, j, array)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    getPermutations([1, 2, 3])
