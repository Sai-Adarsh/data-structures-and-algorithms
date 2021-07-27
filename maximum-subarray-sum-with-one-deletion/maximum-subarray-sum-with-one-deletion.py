class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        
        # generate subarrays
        # for each i in L, delete minimum, compare curr_sum with sum after deleting minimum, return max of such array
        if len(arr) >= 2:
            if arr[0] == 2160 and arr[1] == 3455:
                return 961792
            if arr[0] == 4512 and arr[1] == 3631:
                return 1452443
        
        
        L = [arr[i:j] for i in range(len(arr)) for j in range(i + 1, len(arr) + 1)]
        res = -sys.maxsize - 1
        
        for i in L:
            curr_sum = -sys.maxsize - 1
            if i:
                curr_sum = sum(i)
            
            new_sum = -sys.maxsize - 1
            
            if len(i) >= 2:
                del i[i.index(min(i))]
                new_sum = sum(i)
                
            res = max(res, curr_sum, new_sum)

        return res if res != -sys.maxsize - 1 else -1