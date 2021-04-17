class ProductOfNumbers:
    from numpy import prod
    def __init__(self):
        self.L = []
        
    def add(self, num: int) -> None:
        self.L.append(num)

    def getProduct(self, k: int) -> int:
        return prod(self.L[len(self.L) - k : len(self.L)])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)