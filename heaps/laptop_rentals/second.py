# better time complexity than solution 1, but worse space complexity
# O(nlog(n)) time | O(n) space
def laptopRentals(times: list):
    if not times:
        return 0
    starts = [i[0] for i in sorted(times, key=lambda x: x[0])]
    ends = [i[1] for i in sorted(times, key=lambda x: x[1])]
    i = j = laptops = 0
    while i < len(starts):
        if starts[i] < ends[j]:
            laptops += 1
        else:
            j += 1
        i += 1
    return laptops


if __name__ == '__main__':
    data = [
        [0, 2],
        [1, 4],
        [4, 6],
        [0, 4],
        [7, 8],
        [9, 11],
        [3, 10]
    ]
    res = laptopRentals(data)
    print(res)
