class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        
        left = 0
        right = 0
        res = []
        while left < len(A) or right < len(B):
            try:
                if A[left][0] <= B[right][1] and A[left][1] >= B[right][0]:
                    res.append([max(A[left][0], B[right][0]), min(A[left][1], B[right][1])])
                if A[left][1] >= B[right][1]:
                    right += 1
                else:
                    left += 1
            except:
                break
        return res