class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        L = list(map(list, collections.Counter(arr).items()))
        L.sort(key = lambda x: x[1], reverse = True)
        L = [i[1] for i in L]
        res = 0
        
        for i in range(len(L)):
            res += L[i]
            if res >= len(arr) // 2:
                return i + 1