class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        
        # Naive brute force approach using for loop and slicing
        A = arr
        n = len(A)
        indexes = [i for i in range(n) if A[i] == 1]
        m = len(indexes)
        
        if m == 0: return [0, 2]
        
        if m % 3 != 0: return [-1, -1]
        p1, p2 = indexes[0], indexes[m//3-1]
        p3, p4 = indexes[m//3], indexes[2*m//3-1]
        p5, p6 = indexes[2*m//3], indexes[-1]
        part1, part2, part3 = A[p1:p2+1], A[p3:p4+1], A[p5:p6+1]
        
        if part1 != part2 or part2 != part3: return [-1, -1]
        
        l1 = p3 - p2 - 1
        l2 = p5 - p4 - 1
        l3 = n - p6 - 1
        
        if l3 > l2 or l3 > l1: return [-1, -1]
        
        return [p2 + l3, p4 + l3 + 1]