class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        return self.backTracking([], [], s, 0)
        
    def backTracking(self, res, curr_path, s, start):
        # our goal
        # base case
        if start == 4 and not s:
            res.append(".".join(curr_path))
            return
        
        # our constraints
        # recursive case
        if len(s) > (4 - start) * 3 or len(s) < (4 - start):
            return
        
        # our choice
        for i in range(min(3 if s[0] != "0" else 1, len(s))):
            sub_sting = s[:i + 1]
            if int(sub_sting) < 256:
                self.backTracking(res, curr_path + [sub_sting], s[i + 1:], start + 1)
        
        return res
        
        