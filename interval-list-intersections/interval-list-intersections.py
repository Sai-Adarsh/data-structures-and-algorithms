class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a_ptr = 0
        b_ptr = 0
        res = []
        
        while a_ptr < len(A) or b_ptr < len(B):
            try:
                if A[a_ptr][0] <= B[b_ptr][1] and A[a_ptr][1] >= B[b_ptr][0]:
                    res.append([max(A[a_ptr][0], B[b_ptr][0]), min(A[a_ptr][1], B[b_ptr][1])])
                if A[a_ptr][1] >= B[b_ptr][1]:
                    b_ptr += 1
                else:
                    a_ptr += 1
            except:
                break
        return res
