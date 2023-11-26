# https://www.algoexpert.io/questions/shifted-binary-search

# O(log(n)) time | O(1) space
def shiftedBinarySearch(array, target):
    l, r = 0, len(array) - 1
    while l <= r:
        mid = (l + r) // 2
        if array[mid] == target:
            return mid
        if array[l] <= array[mid]:  # l --> mid is sorted
            if array[l] <= target < array[mid]:  # target in (l --> mid) sorted part
                r = mid - 1
            else:
                l = mid + 1
        else:  # mid --> r is sorted
            if array[mid] < target <= array[r]:  # target in (mid --> r) sorted part
                l = mid + 1
            else:
                r = mid - 1
    return -1
