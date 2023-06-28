class MinStack:

    def __init__(self):
        self.stack = []
        self.insortDs = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        bisect.insort(self.insortDs, val)


    def pop(self) -> None:
        if self.stack:
            temp = self.stack.pop()
            self.insortDs.remove(temp)
            return temp

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.insortDs:
            return self.insortDs[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()