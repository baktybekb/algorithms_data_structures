import math
from typing import List


# O(n) time | O(1) space
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        value1 = int(math.sqrt(area))
        while area % value1 != 0:
            value1 -= 1
        return [area // value1, value1]
