class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        
        L = list(map(list, collections.Counter(arr).items()))
        L.sort(key = lambda x: x[1], reverse = True)
        L = [i[1] for i in L]
        
        start = 0
        curr_sum = 0
        
        for i in L:
            curr_sum += i
            start += 1
            
            if curr_sum >= len(arr) // 2:
                return start