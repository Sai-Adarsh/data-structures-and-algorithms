class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        return self.backTracking([], s, [], 0)
        return self.res
        
    def backTracking(self, res, s, curr_path, step):
        # our goal
        if step == 4 and not s:
            res.append(".".join(curr_path))
            return
        
        if len(s) > (4 - step) * 3 or len(s) < (4 - step):
            return
        
        for i in range(min(3 if s[0] != '0' else 1 , len(s))):
            # our constraint
            if int(s[:i + 1]) < 256: 
            #our choice
                self.backTracking(res, s[i + 1:], curr_path + [s[:i + 1]], step + 1)
        return res