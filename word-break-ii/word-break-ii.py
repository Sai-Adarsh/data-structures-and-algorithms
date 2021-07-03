class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def backTracking(res, curr_path, s):
            if not s:
                temp = " ".join(curr_path)
                if temp not in res:
                    res.append(temp)

            for i in range(1, len(s) + 1):
                sub_string = s[0 : i]
                if sub_string in wordDict:
                    backTracking(res, curr_path + [sub_string], s[i : ])

            return res

        L = backTracking([], [], s)
        return (L)