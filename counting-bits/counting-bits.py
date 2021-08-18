class Solution:
    def countBits(self, n: int) -> List[int]:
        
        
        # Naive brute force approach
        L = [bin(i).replace("0b", "").count("1") for i in range(n + 1)]
        return L