def bubble_sort(array):
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] <= array[i + 1]:
                continue
            swap(array, i, i + 1)
            is_sorted = False
    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j - 1, j)
            j -= 1
    return array


def selection_sort(array):
    for i in range(len(array) - 1):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] >= array[min_idx]:
                continue
            min_idx = j
        if i == min_idx:
            continue
        swap(array, i, min_idx)


def quick_sort(array):
    helper(array, 0, len(array) - 1)
    return array


def helper(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(array, left, right)
        elif array[left] <= array[pivot]:
            left += 1
        elif array[right] >= array[pivot]:
            right -= 1
    swap(array, pivot, right)
    smaller_left = right - 1 - start < end - (right + 1)
    if smaller_left:
        helper(array, start, right - 1)
        helper(array, right + 1, end)
    else:
        helper(array, right + 1, end)
        helper(array, start, right - 1)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def heap_sort(array):
    build_heap(array)
    for i in reversed(range(1, len(array))):
        swap(array, 0, i)
        sift_down(array, 0, i - 1)
    return array


def build_heap(array):
    last_parent_idx = (len(array) - 2) // 2
    for current_idx in reversed(range(last_parent_idx + 1)):
        sift_down(array, current_idx, len(array) - 1)
    return array


def sift_down(array, current_idx, end_idx):
    child_one_idx = current_idx * 2 + 1
    while child_one_idx <= end_idx:
        child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
        if child_two_idx != -1 and array[child_two_idx] > array[child_one_idx]:
            idx_to_swap = child_two_idx
        else:
            idx_to_swap = child_one_idx
        if array[idx_to_swap] > array[current_idx]:
            swap(array, current_idx, idx_to_swap)
            current_idx = idx_to_swap
            child_one_idx = current_idx * 2 + 1
        else:
            break


if __name__ == '__main__':
    data = [8, 5, 2, 9, 5, 6, 3]
    # selection_sort(data)
    # quick_sort(data)
    # heap_sort(data)
    insertion_sort(data)
    print(data)
