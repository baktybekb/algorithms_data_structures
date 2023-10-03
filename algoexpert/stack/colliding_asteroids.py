# https://www.algoexpert.io/questions/colliding-asteroids

# O(n) time | O(n) space
def collidingAsteroids(array):
    stack = []
    for val in array:
        if val > 0:
            stack.append(val)
            continue
        while True:
            if not stack or stack[-1] < 0:
                stack.append(val)
                break
            if stack[-1] == abs(val):
                stack.pop()
                break
            if stack[-1] > abs(val):
                break
            stack.pop()
    return stack


if __name__ == '__main__':
    assert collidingAsteroids([-3, 5, -8, 6, 7, -4, -7]) == [-3, -8, 6]
