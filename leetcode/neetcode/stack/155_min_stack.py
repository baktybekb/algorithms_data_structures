# O(1) time for each method, O(1) space
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            min_val = min(self.min_stack[-1], val)
            self.min_stack.append(min_val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.min_stack.pop()
        return val

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
