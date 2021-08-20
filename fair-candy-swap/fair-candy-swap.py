class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        Sa, Sb = sum(aliceSizes), sum(bobSizes)
        setB = set(bobSizes)
        for x in aliceSizes:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]