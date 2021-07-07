class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.L = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.L[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        
        nums = self.L[key]
        left = 0
        right = len(nums)
        
        while left < right:
            curr = left + (right - left) // 2
            if nums[curr][0] <= timestamp:
                left = curr + 1
            elif nums[curr][0] > timestamp:
                right = curr
                
        return "" if right == 0 else nums[right - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)