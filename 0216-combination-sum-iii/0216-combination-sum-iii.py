class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backTracking(currList, finalList, n, j):
            if len(currList) == k and n == 0:
                finalList.append(currList)
            
            for i in range(j, 10):
                if i not in currList and n - i >= 0:
                    backTracking(currList + [i], finalList, n - i, i + 1)
            
            return finalList

        return backTracking([], [], n, 1)