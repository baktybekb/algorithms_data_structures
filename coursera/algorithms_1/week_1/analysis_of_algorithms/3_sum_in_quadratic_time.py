"""
Problem:
    3-SUM in quadratic time. Design an algorithm for the 3-SUM problem that takes time proportional to n^2
    in the worst case. You may assume that you can sort the n integers in time proportional to n^2 or better.
"""


def three_sum(array, target):
    array.sort()
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            cur_sum = array[i] + array[left] + array[right]
            if cur_sum == target:
                return True
            elif cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
    return False


if __name__ == '__main__':
    res = three_sum(array=[12, 3, 1, 2, -6, 5, -8, 6], target=0)
    print(res)
