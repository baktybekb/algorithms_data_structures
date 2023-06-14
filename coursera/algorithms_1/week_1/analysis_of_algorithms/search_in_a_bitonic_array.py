"""
Problem:
    Search in a bitonic array.
    An array is bitonic if it is comprised of an increasing sequence of
    integers followed immediately by a decreasing sequence of integers. Write a program that, given a bitonic array of
    n distinct integer values, determines whether a given integer is in the array.

    Standard version: Use ∼3lgn compares in the worst case.
    Signing bonus: Use ∼2lgn compares in the worst case (and prove that no algorithm can guarantee to perform fewer than
    ∼2lgn compares in the worst case).
"""
import unittest


def find_peak(array):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > array[mid + 1] and array[mid] > array[mid - 1]:
            return mid, array[mid]
        if array[mid] < array[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1


def search_key(array, left, right, target, increasing=True):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        if increasing:
            if array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if array[mid] < target:
                right = mid - 1
            else:
                left = mid + 1
    return None


# 3log(n)
def bitonic_search(array, target):
    peak_idx, peak = find_peak(array)
    if peak == target:
        return peak_idx
    left_idx = search_key(array, 0, peak_idx, target)
    right_idx = search_key(array, peak_idx + 1, len(array) - 1, target, increasing=False)
    if not left_idx and not right_idx:
        return -1
    return left_idx if left_idx is not None else right_idx


class TestClass(unittest.TestCase):
    def test_func(self):
        array = [1, 3, 5, 9, 12, 14, 20, 24, 19, 16, 7, 3, 1]
        self.assertEqual(bitonic_search(array, 1), 0)
        self.assertEqual(bitonic_search(array, 24), 7)
        self.assertEqual(bitonic_search(array, 16), 9)
        self.assertEqual(bitonic_search(array, 50), -1)

