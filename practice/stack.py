# Coding problem: find pairs with no intersections

# O(nlog(n)) time | O(n) space
def run(product):
    product.sort(key=lambda x: x[0])
    stack = []
    left = right = float('-inf')
    for start, end in product:
        if start < right:
            left, right = min(left, start), max(right, end)
            if stack:
                stack.pop()
        else:
            left, right = start, end
            stack.append([start, end])
    return stack


if __name__ == '__main__':
    assert run(product=[[1, 3], [2, 4], [4, 6], [6, 8]]) == [[4, 6], [6, 8]]
    assert run(product=[[1, 3], [2, 4], [0, 5], [6, 8], [8, 9], [8, 10]]) == [[6, 8]]
    assert run(product=[[8, 9], [8, 10], [1, 3], [2, 4], [0, 5], [6, 8]]) == [[6, 8]]
