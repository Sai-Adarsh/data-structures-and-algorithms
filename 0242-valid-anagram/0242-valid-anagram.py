class Solution:
    def populateMap(self, s):
        hashMap = {}
        for i in s:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        return hashMap

    def isAnagram(self, s: str, t: str) -> bool:
        return self.populateMap(s) == self.populateMap(t)