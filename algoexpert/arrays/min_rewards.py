# https://www.algoexpert.io/questions/min-rewards

# O(n) time | O(n) space
def minRewards(array):
    rewards = [1] * len(array)
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed(range(len(array) - 1)):
        if array[i] > array[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)


if __name__ == '__main__':
    assert minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]) == 25
    assert minRewards([0, 4, 2, 1, 3]) == 9



