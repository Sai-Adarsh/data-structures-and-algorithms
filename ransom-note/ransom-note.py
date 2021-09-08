class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Is subsequence
        
        ransomNote = [_ for _ in ransomNote]
        ransomNote.sort()
        
        magazine = [_ for _ in magazine]
        magazine.sort()
        
        if len(magazine) < len(ransomNote):
            return False
        
        left = 0
        right = 0
        
        while left < len(ransomNote) and right < len(magazine):
            if ransomNote[left] == magazine[right]:
                left += 1
            right += 1
                
        
        return left == len(ransomNote)