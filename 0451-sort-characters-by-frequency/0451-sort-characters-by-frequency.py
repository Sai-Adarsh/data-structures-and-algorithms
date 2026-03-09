class Solution:
    def frequencySort(self, s: str) -> str:
        hashMap = collections.Counter(s)

        hashMapList = [(i, j) for i, j in hashMap.items()]
        hashMapList.sort(key = lambda x: x[1], reverse = True)

        res = ""
        for i, j in hashMapList:
            res += (i * j)
        
        return res