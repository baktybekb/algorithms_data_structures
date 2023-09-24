# O(n) time | O(n) space
def sortedSquaredArray(array):
    l, r = 0, len(array) - 1
    res = [0] * len(array)
    for idx in reversed(range(len(array))):
        abs_l = abs(array[l])
        abs_r = abs(array[r])
        if abs_l > abs_r:
            res[idx] = abs_l * abs_l
            l += 1
        else:
            res[idx] = abs_r * abs_r
            r -= 1
    return res

