class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []
        for eachNum in range(n + 1):
            res.append(bin(eachNum).replace("0b", "").count("1"))
        
        return res