class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        
        overlap = 0
        if C <= E or A >= G or D <= F or B >= H: 
            overlap = 0
        else:
            overlap =  (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        return area1 + area2 - overlap