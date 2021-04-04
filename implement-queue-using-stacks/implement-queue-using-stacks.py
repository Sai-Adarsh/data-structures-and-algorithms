class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.stack = deque([])
        
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack:
            return self.stack.popleft()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack:
            return self.stack[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if self.stack else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()