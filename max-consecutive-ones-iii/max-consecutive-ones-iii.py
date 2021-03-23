class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        right = 0
        
        res = 0
        
        while right <= len(A) - 1:
            if A[right] == 0:
                K -= 1
            if K < 0:
                if A[left] == 0:
                    K += 1
                left += 1
            right += 1
                
            
            
        return right - left