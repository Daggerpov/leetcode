"""
Maintain two stacks, one for overall values, and one for the minimum at that current value. Such that, pop pops from both stacks, top checks overall stack, and getmin checks min stack. Push will always append to overall stack, but will only append the minimum of the current minimum vs. this new val. Minimums in minStack could be repeated, and corresponded to current values up until that point of stack.
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            # minStack exists
            self.minStack.append(min(self.getMin(), val))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1] # current min
