class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        
        
        sortedA = sorted(A)
        sortedB = sorted(B)
        
        greater_than = {b: [] for b in B}
        remaining = []
        
        j = 0
        for each_a in sortedA:
            if each_a > sortedB[j]:
                greater_than[sortedB[j]].append(each_a)
                j += 1
            else:
                remaining.append(each_a)
                
        return [greater_than[b].pop() if greater_than[b] else remaining.pop() for b in B]