class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)

        def isSub(s, sub):
            i = 0
            j = 0
            while i < len(s) and j < len(sub):
                if s[i] == sub[j]:
                    j += 1
                i += 1
            return j == len(sub)

        
        memo = {}
        def backTracking(curr_path, start):
            if start in memo:
                return memo[start]
            if start == len(words):
                return len(curr_path)

            res = 0
            for i in range(start, len(words)):
                if not curr_path:
                    res = max(res, backTracking(curr_path + [words[i]], i + 1))
                else:
                    if len(words[i]) - len(curr_path[-1]) == 1:
                        if isSub(words[i], curr_path[-1]):
                            res = max(res, backTracking(curr_path + [words[i]], i + 1))
                        else:
                            res = max(res, len(curr_path))
                    else:
                        res = max(res, len(curr_path))
            memo[start] = res
            return memo[start]
        L = backTracking([], 0)
        return L