class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        i = 0 
        while i < num + 1:
            res.append(bin(i).replace("0b", "").count('1'))
            i += 1
        return res