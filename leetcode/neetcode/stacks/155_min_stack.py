# https://leetcode.com/problems/min-stack/description/


# O(1) time each method
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.stack:
            min_val = min(self.min_stack[-1], val)
        else:
            min_val = val
        self.stack.append(val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.min_stack.pop()
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
