# Best    O(n) time | O(1) space
# Average O(n) time | O(1) space
# Worst   O(n^2) time | O(1) space
def quickselect(array, k):
    k = k - 1
    helper(0, len(array) - 1, array, k)
    return array[k]


def helper(start, end, array, k):
    while True:
        if start >= end:
            return
        pivot = start
        left = start + 1
        right = end
        while left <= right:
            if array[left] > array[pivot] and array[right] < array[pivot]:
                swap(array, left, right)
            if array[left] <= array[pivot]:
                left += 1
            if array[right] >= array[pivot]:
                right -= 1
        swap(array, pivot, right)
        if right == k:
            break
        elif right > k:
            end = right - 1
        elif right < k:
            start = right + 1


def swap(array, i, j):
    array[j], array[i] = array[i], array[j]


if __name__ == "__main__":
    quickselect([8, 5, 2, 9, 7, 6, 3], 3)
