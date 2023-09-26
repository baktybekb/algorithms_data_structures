# https://www.algoexpert.io/questions/sweet-and-savory

# O(nlog(n)) time | O(1) space
def sweetAndSavory(dishes, target):
    res = [0, 0]
    dishes.sort()
    min_diff = float('inf')
    l, r = 0, len(dishes) - 1
    while l < r and dishes[l] < 0 and dishes[r] > 0:
        flavor = dishes[l] + dishes[r]
        if flavor <= target:
            diff = target - flavor
            if diff < min_diff:
                min_diff = diff
                res = [dishes[l], dishes[r]]
            l += 1
        else:
            r -= 1
    return res


if __name__ == '__main__':
    assert sweetAndSavory(dishes=[-5, 10], target=4) == [0, 0]
    assert sweetAndSavory(dishes=[-5, -3, 1, 7], target=8) == [-3, 7]
