# O(2^n * n) time | O(n^2 * n) space
def powerset(array, idx=None):
    if not array:
        return [[]]
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
    val = array[idx]
    subsets = powerset(array, idx - 1)
    for i in range(len(subsets)):
        subsets.append(subsets[i] + [val])
    return subsets


if __name__ == '__main__':
    res = powerset([1, 2, 3])
    assert res == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
