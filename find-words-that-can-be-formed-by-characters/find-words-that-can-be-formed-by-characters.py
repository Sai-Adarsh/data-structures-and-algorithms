class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        chars_count = Counter(chars)
        
        res = 0
        for i in range(len(words)):
            not_possible = False
            for j in words[i]:
                if words[i].count(j) > chars_count[j]:
                    not_possible = True
            if not_possible == False:
                res += len(words[i])
        return res
            
                