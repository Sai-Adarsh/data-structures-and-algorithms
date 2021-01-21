class MinStack:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L = []
    def push(self, x: int) -> None:
        self.L.append(x)
​
    def pop(self) -> None:
        self.L.pop()
​
    def top(self) -> int:
        return self.L[-1]
​
    def getMin(self) -> int:
        return min(self.L)
​
