class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        patterns = []
        
        for i in matrix:
            hash_map = {}
            count = 0
            L = []
            for j in i:
                if j not in hash_map:
                    hash_map[j] = count
                    count += 1
                L.append(hash_map[j])
            patterns.append(tuple(L))
            
        hash_map = collections.Counter(patterns).values()
        return max(hash_map)