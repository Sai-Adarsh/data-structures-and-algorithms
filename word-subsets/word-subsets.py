class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        
        h = {}
        for word in words2:
            m = defaultdict(int)
            for w in word:
                m[w] += 1
                if(w not in h):
                    h[w] = m[w]
                else:
                    h[w] = max(h[w], m[w])
                    
        res = []
        for word in words1:
            m = h.copy()
            for w in word:
                if(w in m):
                    m[w] -= 1
                    if(m[w] == 0):
                        del m[w]
            if(len(m) == 0):
                res.append(word)
        return res