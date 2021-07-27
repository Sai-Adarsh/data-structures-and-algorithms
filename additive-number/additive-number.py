class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        # backTracking approach
        
        def backTracking(curr_path, start):
            if start == len(num):
                if len(curr_path) >= 3:
                    return 1
                return 0
            
            
            res = 0
            for i in range(start + 1, len(num) + 1):
                sub_string = num[start : i]
                if len(sub_string) == len(str(int(sub_string))):
                    if len(curr_path) <= 1:
                        res += backTracking(curr_path + [int(sub_string)], i)
                    else:
                        if int(sub_string) == curr_path[-1] + curr_path[-2]:
                            res += backTracking(curr_path + [int(sub_string)], i)
                        else:
                            continue
                            
            return res
        
        L = backTracking([], 0)
        return L >= 1