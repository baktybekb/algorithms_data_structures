# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    res = []
    cur_range = range(len(buildings))
    traverse = cur_range if direction == 'WEST' else reversed(cur_range)
    max_val = 0
    for i in traverse:
        if buildings[i] > max_val:
            max_val = buildings[i]
            res.append(i)
    return res if direction == 'WEST' else sort_array(res)


# O(n) time | O(1) space
def sort_array(array):
    l, r = 0, len(array) - 1
    while l < r:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1
    return array
