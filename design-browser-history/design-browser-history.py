class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.arr = []
        
        self.arr.append(homepage)
        self.curr_pos = len(self.arr)

    def visit(self, url: str) -> None:
        self.arr[:] = self.arr[:self.curr_pos + 1]
        self.curr_pos = len(self.arr)
        self.arr.append(url)

    def back(self, steps: int) -> str:
        if steps > self.curr_pos:
            self.curr_pos = 0
        else:
            self.curr_pos -= steps
        return self.arr[self.curr_pos]

    def forward(self, steps: int) -> str:
        if steps > len(self.arr) - self.curr_pos - 1:
            self.curr_pos = len(self.arr) - 1
        else:
            self.curr_pos += steps
        return self.arr[self.curr_pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)