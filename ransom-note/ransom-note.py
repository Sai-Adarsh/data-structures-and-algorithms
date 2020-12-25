​
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections
        ransomNote = [x for x in ransomNote]
        magazine = [x for x in magazine]
        for i in range(0, len(ransomNote)):
            try:
                indexing = magazine.index(ransomNote[i])
                magazine[indexing] = None
            except:
                continue
        count = magazine.count(None)
        if len(ransomNote) == count:
            return True
        else:
            return False    
