class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n).replace("0b", "").zfill(32)[::-1], 2)