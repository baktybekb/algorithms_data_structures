# https://www.algoexpert.io/questions/min-max-stack-construction

# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.min_max = []
        self.stack = []

    def peek(self):
        return self.stack[-1] if self.stack else None

    def pop(self):
        if not self.stack:
            return None
        val = self.stack.pop()
        self.min_max.pop()
        return val

    def push(self, number):
        if not self.stack:
            self.min_max.append((number, number))
        else:
            self.min_max.append(
                (min(self.min_max[-1][0], number), max(self.min_max[-1][1], number))
            )
        self.stack.append(number)

    def getMin(self):
        if not self.stack:
            return None
        return self.min_max[-1][0]

    def getMax(self):
        if not self.stack:
            return None
        return self.min_max[-1][1]
