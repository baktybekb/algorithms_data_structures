from typing import List


# O(n) time | O(n) space
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = {}
        for num in nums:
            if num in mapper:
                mapper[num] += 1
            else:
                mapper[num] = 1
        array = [None for _ in range(len(nums) + 1)]
        for key, val in mapper.items():
            if not array[val]:
                array[val] = [key]
                continue
            array[val].append(key)
        res = []
        for i in reversed(range(len(array))):
            if k == 0:
                return res
            if not array[i]:
                continue
            res.extend(array[i])
            k -= len(array[i])


if __name__ == '__main__':
    sol = Solution()
    assert sol.topKFrequent([4, 1, -1, 2, -1, 2, 3], k=2) == [-1, 2]
