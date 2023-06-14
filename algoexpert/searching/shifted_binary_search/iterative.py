# O(log(n)) time | O(1) space
def shiftedBinarySearch(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        if array[left] <= array[mid]:
            # left side is sorted
            if array[left] <= target < array[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # left side is unsorted --> right side is sorted
            if array[mid] < target <= array[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
