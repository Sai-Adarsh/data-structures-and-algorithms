class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict({})
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        temp = self.cache[key]
        del self.cache[key]
        self.cache[key] = temp
        return temp

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last = False)
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)