class MedianFinder:

    def __init__(self):
        self.res = []
        self.resLen = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.res, num)
        self.resLen += 1

    def findMedian(self) -> float:
        if self.resLen % 2 == 0:
            index = self.resLen // 2
            return (self.res[index] + self.res[index - 1]) / 2
        else:
            index = self.resLen // 2
            return self.res[index]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()