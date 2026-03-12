class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapOne = {}
        hashMapTwo = {}
        for i in s:
            if i not in hashMapOne:
                hashMapOne[i] = 1
            else:
                hashMapOne[i] += 1
        
        for i in t:
            if i not in hashMapTwo:
                hashMapTwo[i] = 1
            else:
                hashMapTwo[i] += 1
        
        return hashMapOne == hashMapTwo