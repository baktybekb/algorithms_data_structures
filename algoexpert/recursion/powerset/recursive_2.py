def powerset(array, i=None):
    if not array:
        return [[]]
    if i is None:
        i = len(array) - 1
    elif i < 0:
        return [[]]
    val = array[i]
    subsets = powerset(array, i - 1)
    for i in range(len(subsets)):
        subsets.append(subsets[i] + [val])
    return subsets
