def threeNumberSum(array, targetSum):
    res = []
    array.sort()
    for idx in range(len(array) - 2):
        l = idx + 1
        r = len(array) - 1
        while l < r:
            current = array[l] + array[r] + array[idx]
            if current < targetSum:
                l += 1
            elif current > targetSum:
                r -= 1
            else:
                res.append([array[idx], array[l], array[r]])
                l += 1
                while l < r and array[l - 1] == array[l]:  # additional check for duplicates, look at testcase 2
                    l += 1
    return res


if __name__ == '__main__':
    assert threeNumberSum(array=[12, 3, 1, 2, -6, 5, -8, 6], targetSum=0) == [
        [-8, 2, 6],
        [-8, 3, 5],
        [-6, 1, 5]
    ]
    assert threeNumberSum(array=[12, 3, 1, 3, -6, 5, -8, 5], targetSum=0) == [[-8, 3, 5], [-6, 1, 5], [-6, 3, 3]]
