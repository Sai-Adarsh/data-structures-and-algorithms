class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        one = ""
        two = ""
        
        for i in word1:
            one += i
        for i in word2:
            two += i
        return one == two
