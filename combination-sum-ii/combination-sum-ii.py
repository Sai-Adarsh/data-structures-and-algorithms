class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        return self.backTracking(candidates, [], [], 0, target)
    
    def backTracking(self, candidates, result, curr_path, divider, target):
        if target <= 0:
            if target == 0:
                if sorted(curr_path) not in result:
                    result.append(sorted(curr_path))
                    
            return
        for i in range(divider, len(candidates)):
            if i > divider and candidates[i] == candidates[i - 1]:
                continue
            self.backTracking(candidates, result, curr_path + [candidates[i]], i + 1, target - candidates[i])

        return result