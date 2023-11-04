# O(nlog(n)) time | O(n) space
def laptopRentals(times):
    start_data = sorted((i[0] for i in times))
    end_data = sorted((i[1] for i in times))
    start, end = 0, 0
    laptops = 0
    while start < len(start_data) and end < len(end_data):
        if start_data[start] < end_data[end]:
            laptops += 1
        else:
            end += 1
        start += 1
    return laptops
