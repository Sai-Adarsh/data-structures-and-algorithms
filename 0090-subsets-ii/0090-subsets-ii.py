class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backTracking(curr, indices, final, currLen, j):
            if len(curr) == currLen:
                if sorted(curr) not in final:
                    final.append(sorted(curr))
                return
            for i in range(j, len(nums)):
                if i not in indices:
                    backTracking(curr + [nums[i]], indices + [i], final, _, i + 1)
            return final
        res = []
        for _ in range(len(nums) + 1):
            if _ == 0:
                res += [[]]
            else:
                res += backTracking([], [], [], _, 0)
        
        return res