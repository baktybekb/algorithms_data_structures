def searchForRange(array, target):
    result = [-1, -1]
    search(array, target, result, go_left=True)
    search(array, target, result, go_left=False)
    return result


def search(array, target, result, go_left):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            if go_left:
                if mid == 0 or array[mid - 1] != target:
                    result[0] = mid
                    return
                else:
                    right = mid - 1
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    result[1] = mid
                    return
                else:
                    left = mid + 1
