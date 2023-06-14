# O(log(n)) time | O(log(n)) space
def searchForRange(array, target):
    result = [-1, -1]
    left, right = 0, len(array) - 1
    search(left, right, array, target, result, go_left=True)
    search(left, right, array, target, result, go_left=False)
    return result


def search(left, right, array, target, result, go_left):
    if left > right:
        return
    mid = (left + right) // 2
    if array[mid] < target:
        search(mid + 1, right, array, target, result, go_left)
    elif array[mid] > target:
        search(left, mid - 1, array, target, result, go_left)
    else:
        if go_left:
            if mid == 0 or array[mid - 1] != target:
                result[0] = mid
                return
            else:
                search(left, mid - 1, array, target, result, go_left)
        else:
            if mid == len(array) - 1 or array[mid + 1] != target:
                result[1] = mid
                return
            else:
                search(mid + 1, right, array, target, result, go_left)
