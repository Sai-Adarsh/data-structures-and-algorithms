class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).replace("0b", "").count("1") for i in range(n + 1)]