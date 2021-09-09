class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        
        hash_map = defaultdict(list)
        for i in range(len(s) - len(p) + 1):
            L = s[i : i + len(p)]
            L = sorted(L)
            hash_map[tuple(L)].append(i)
            
        return hash_map[tuple(sorted(p))]