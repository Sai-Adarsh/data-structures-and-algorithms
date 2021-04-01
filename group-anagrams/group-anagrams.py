class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}
        
        for i in strs:
            if tuple(sorted(i)) not in res:
                res[tuple(sorted(i))] = [i]
            else:
                res[tuple(sorted(i))].append(i)
                
        return list(map(list, (res.values())))