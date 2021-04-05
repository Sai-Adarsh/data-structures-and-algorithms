class FreqStack:

    def __init__(self):
        from collections import Counter
        self.L = Counter()
        self.group = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        
        temp = self.L[val] + 1
        self.L[val] = temp
        
        if temp > self.maxFreq:
            self.maxFreq = temp
        if temp not in self.group:
            self.group[temp] = [val]
        else:
            self.group[temp].append(val)
        
    def pop(self) -> int:
        x = self.group[self.maxFreq].pop()
        self.L[x] -= 1
        
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()