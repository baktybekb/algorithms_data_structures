# https://www.algoexpert.io/questions/four-number-sum

# O(n ^ 2) time | O(n ^ 2) space
def fourNumberSum(array, target_sum):
    res = []
    sums = {}
    for i in range(1, len(array)):
        for r in range(i + 1, len(array)):
            diff = target_sum - (array[i] + array[r])
            if diff not in sums:
                continue
            for item in sums[diff]:
                res.append([array[i], array[r], *item])
        for l in range(i):
            cur_sum = array[l] + array[i]
            if cur_sum in sums:
                sums[cur_sum].append([array[l], array[i]])
            else:
                sums[cur_sum] = [[array[l], array[i]]]
    return res


if __name__ == '__main__':
    assert fourNumberSum(array=[7, 6, 4, -1, 1, 2], target_sum=16) == [[4, -1, 7, 6], [1, 2, 7, 6]]
