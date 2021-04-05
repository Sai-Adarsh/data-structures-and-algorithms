class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        x = val
        f = self.freq[x] + 1
        self.freq[x] = f
        
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self) -> int:
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        
        if not self.group[self.maxfreq]:
            self.maxfreq -=1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()