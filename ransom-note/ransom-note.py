class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = [x for x in ransomNote]
        magazine = [x for x in magazine]
        for i in ransomNote:
            try:
                magazine[magazine.index(i)] = None
            except:
                continue
            
        return len(ransomNote) == magazine.count(None)
