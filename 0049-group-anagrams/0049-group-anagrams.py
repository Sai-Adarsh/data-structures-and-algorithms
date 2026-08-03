class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for eachStr in strs:
            hashMap[str(sorted(eachStr))].append(eachStr)
        return [val for val in hashMap.values()]