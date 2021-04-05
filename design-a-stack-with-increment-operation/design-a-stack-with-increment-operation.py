class CustomStack:

    def __init__(self, maxSize: int):
        self.L = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.L) + 1 <= self.maxSize:
            self.L.append(x)

    def pop(self) -> int:
        if self.L:
            return self.L.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        if k <= len(self.L):
            for i in range(k):
                self.L[i] += val
        else:
            for i in range(len(self.L)):
                self.L[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)