class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        return self.backTracking([], [], 0, s)
        
    def backTracking(self, res, curr_path, address_count, s):
        
        # our goal
        # base case
        if address_count == 4 and (len(s) == 0 or not s):
            res.append(".".join(curr_path))
            return
        
        if len(s) > (4 - address_count) * 3 or len(s) < (4 - address_count):
            return
        # our constraint
        for splitter in range(min(3 if s[0] != "0" else 1, len(s))):
            sub_string = s[:splitter + 1]
            if int(sub_string) < 256:
                # our choice:
                self.backTracking(res, curr_path + [s[: splitter + 1]], address_count + 1, s[splitter + 1 :])
        
        
        return res