class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # Store the minimum value at each level
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Main Program
min_stack = MinStack()

min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)

print("Minimum:", min_stack.getMin())  # -3

min_stack.pop()

print("Top:", min_stack.top())         # 0
print("Minimum:", min_stack.getMin())  # -2