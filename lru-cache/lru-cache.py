class LRUCache:

    def __init__(self, capacity: int):
        self.hash_map = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        found = self.hash_map.pop(key)
        self.hash_map[key] = found
        return found

    def put(self, key: int, value: int) -> None:
        
        if key in self.hash_map:
            found = self.hash_map.pop(key)
        elif len(self.hash_map) >= self.capacity:
            self.hash_map.popitem(last = False)
        self.hash_map[key] = value
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)