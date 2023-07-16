# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.min_max_stack = []
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        value = self.stack.pop()
        self.min_max_stack.pop()
        return value

    def push(self, number):
        self.stack.append(number)
        if not self.min_max_stack:
            self.min_max_stack.append((number, number))
            return
        new_min = min(self.min_max_stack[-1][0], number)
        new_max = max(self.min_max_stack[-1][1], number)
        self.min_max_stack.append((new_min, new_max))

    def getMin(self):
        return self.min_max_stack[-1][0]

    def getMax(self):
        return self.min_max_stack[-1][1]
