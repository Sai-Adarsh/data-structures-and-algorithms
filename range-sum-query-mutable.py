class NumArray:
​
    def __init__(self, nums: List[int]):
        
        self.L = []
        self.L[:] = nums
    def update(self, i: int, val: int) -> None:
        del self.L[i]
        self.L.insert(i, val)
​
    def sumRange(self, i: int, j: int) -> int:
        return sum(self.L[i:j + 1])
​
​
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
