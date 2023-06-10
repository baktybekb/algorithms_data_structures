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


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    data = [8, 5, 2, 9, 5, 6, 3]
    selection_sort(data)
    print(data)
