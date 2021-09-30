class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        
        if len(set(candyType)) > len(candyType) // 2:
            return len(candyType) // 2
        return len(set(candyType))