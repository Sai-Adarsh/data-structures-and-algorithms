class SnapshotArray:

    def __init__(self, length: int):
        self.L = {}
        self.hash_map = defaultdict(list)
        self.snap_id = 0
        
    def set(self, index: int, val: int) -> None:
        self.L[index] = val

    def snap(self) -> int:
        self.snap_id += 1
        self.hash_map[self.snap_id - 1] = self.L.copy()
        return self.snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.hash_map:
            if index in self.hash_map[snap_id]:
                return self.hash_map[snap_id][index]
        return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)