class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        
        def isSubsequence(s, word):
            i = 0
            j = 0
            
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == len(word)
        
        
        res = ""
        for word in dictionary:
            if len(word) < len(res):
                continue
            else:
                if isSubsequence(s, word):
                    if len(word) > len(res):
                        res = word
                    elif len(word) == len(res):
                        res = min(res, word)
                        
        return res