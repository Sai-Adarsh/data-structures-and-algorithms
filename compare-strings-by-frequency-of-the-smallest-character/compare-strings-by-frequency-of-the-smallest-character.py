class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        
        q_map = [collections.Counter(i) for i in queries]
        w_map = [collections.Counter(i) for i in words]
        q_min = [min(i) for i in queries]
        w_min = [min(i) for i in words]
        
        L = []
        for i in range(len(queries)):
            temp = q_map[i][q_min[i]]
            res = 0
            for j in range(len(words)):
                if temp < w_map[j][w_min[j]]:
                    res += 1
            L.append(res)
            
        return L