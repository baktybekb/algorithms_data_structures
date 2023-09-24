# https://www.algoexpert.io/questions/smallest-difference

# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference(array_one, array_two):
    array_one.sort()
    array_two.sort()
    idx_one = idx_two = 0
    min_diff = float('inf')
    pair = None
    while idx_one < len(array_one) and idx_two < len(array_two):
        val_one, val_two = array_one[idx_one], array_two[idx_two]
        if val_one < val_two:
            idx_one += 1
            diff = val_two - val_one
        elif val_one > val_two:
            idx_two += 1
            diff = val_one - val_two
        else:
            return [val_one, val_one]
        if diff < min_diff:
            min_diff = diff
            pair = [val_one, val_two]
    return pair

