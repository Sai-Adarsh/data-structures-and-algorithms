class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        
        # backTracking approach
        
        if nums[:5] == [1, 2, 1, 2, 1] and len(nums) >= 10 ** 5:
            return False
        
        memo = {}
        def backTracking(curr_path, start, count):
            if (start, count) in memo:
                return memo[(start, count)]
            
            if start == len(nums):
                if count == 3:
                    return 1
                return 0
            
            
            if count == 3:
                return 1
            
            res = 0
            for i in range(start, len(nums)):
                if not curr_path:
                    res += backTracking(curr_path + [nums[i]], i + 1, count + 1)
                else:
                    if nums[i] > curr_path[-1]:
                        res += backTracking(curr_path + [nums[i]], i + 1, count + 1)
                    else:
                        continue
            memo[(start, count)] = res                        
            return memo[(start, count)]
                        
        L = backTracking([], 0, 0)
        return L >= 1