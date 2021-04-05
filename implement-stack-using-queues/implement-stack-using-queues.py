class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q:
            return self.q.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q:
            return self.q[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if self.q else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()