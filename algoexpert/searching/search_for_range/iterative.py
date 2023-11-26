# https://www.algoexpert.io/questions/search-for-range

# O(log(n)) time | O(1) space
def searchForRange(array, target):
    final_range = [-1, -1]
    search(array, 0, len(array) - 1, target, final_range, True)
    search(array, 0, len(array) - 1, target, final_range, False)
    return final_range


def search(array, left, right, target, final_range, go_left):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            if go_left:
                if mid == 0 or array[mid - 1] != target:
                    final_range[0] = mid
                    return
                right = mid - 1
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    final_range[1] = mid
                    return
                left = mid + 1
