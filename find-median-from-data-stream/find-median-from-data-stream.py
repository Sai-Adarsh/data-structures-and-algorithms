class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L = []

    def addNum(self, num: int) -> None:
        
        self.L.append(num)
        self.L.sort()

    def findMedian(self) -> float:
        curr_len = len(self.L)
        if curr_len % 2 == 0:
            curr_len = math.ceil(curr_len / 2)
            return (self.L[curr_len] + self.L[curr_len - 1]) / 2
        else:
            curr_len = curr_len // 2
            return self.L[curr_len]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()