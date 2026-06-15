class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backTracking(currArr, currSum, finalArr, target, j):
            if target == 0:
                if currArr not in finalArr:
                    finalArr.append(currArr)
                return
                
            for i in range(j, len(candidates)):
                if target - candidates[i] > -1:
                    backTracking(currArr + [candidates[i]], currSum + candidates[i], finalArr, target - candidates[i], i)
            
            return finalArr
        return backTracking([], 0, [], target, 0)