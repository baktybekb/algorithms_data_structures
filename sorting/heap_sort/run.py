# O (nlog(n)) time | O(1) space
def heapSort(array):
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


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def sift_down(array, current_idx, end_idx):
    child_one_idx = current_idx * 2 + 1
    while child_one_idx <= end_idx:
        child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
        if child_two_idx != -1 and array[child_two_idx] > array[child_one_idx]:
            idx_to_swap = child_two_idx
        else:
            idx_to_swap = child_one_idx
        if array[idx_to_swap] > array[current_idx]:
            swap(array, idx_to_swap, current_idx)
            current_idx = idx_to_swap
            child_one_idx = current_idx * 2 + 1
        else:
            break


