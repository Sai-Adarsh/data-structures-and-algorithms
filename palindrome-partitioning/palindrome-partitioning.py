class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        return self.backTracking(s, [], 0, [])
        
    def backTracking(self, s, res, start, curr_path,):
        # base case
        if start == len(s):
            res.append(curr_path)
        
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if sub == sub[::-1]:
                self.backTracking(s, res, end, curr_path + [sub])
        return res