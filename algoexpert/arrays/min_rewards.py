# https://www.algoexpert.io/questions/min-rewards

# O(n) time | O(n) space
def minRewards(scores):
    rewards = [1] * len(scores)
    for i in range(1, len(scores)):
        if scores[i - 1] < scores[i]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            if rewards[i] > rewards[i + 1]:
                continue
            rewards[i] = rewards[i + 1] + 1
    return sum(rewards)


if __name__ == '__main__':
    assert minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]) == 25
    assert minRewards([0, 4, 2, 1, 3]) == 9



