class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        overlap = abs(min(C, G) - max(A, E)) * abs(min(D, H) - max(B, F))
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        
        if C <= E or D <= F or G <= A or H <= B:
            overlap = 0
        
        return area1 + area2 - overlap