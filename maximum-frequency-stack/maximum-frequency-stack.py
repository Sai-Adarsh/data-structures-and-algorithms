class FreqStack:

    def __init__(self):
        self.L = collections.Counter()
        self.group = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        temp = self.L[val]
        temp += 1
        self.L[val] = temp
        self.maxFreq = max(self.maxFreq, self.L[val])
        self.group[self.L[val]].append(val)

    def pop(self) -> int:
        curr_stack = self.group[self.maxFreq]
        temp = curr_stack.pop()
        if not curr_stack:
            self.maxFreq -= 1
        self.L[temp] -= 1
        return temp

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()