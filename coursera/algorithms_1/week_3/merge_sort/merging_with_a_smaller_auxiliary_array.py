"""
Problem:
Merging with smaller auxiliary array. Suppose that the subarray a[0] to a[n - 1] is sorted and the subarray
a[n] to a[2*n - 1] is sorted. How can you merge the two subarrays so that a[0] to a[2*n - 1] is sorted using an
auxiliary array of length n (instead of 2n)
Hint: copy only the left half into the auxiliary array.
"""


def do_merge(array):
    mid = len(array) // 2
    auxiliary = array[:mid]
    i = k = 0
    j = mid
    while i < mid and j < len(array):
        if auxiliary[i] <= array[j]:
            array[k] = auxiliary[i]
            i += 1
        else:
            array[k] = array[j]
            j += 1
        k += 1
    while i < mid:
        array[k] = auxiliary[i]
        i += 1
        k += 1
    return array


def test():
    array = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
    do_merge(array)
    print(array)


if __name__ == '__main__':
    test()



