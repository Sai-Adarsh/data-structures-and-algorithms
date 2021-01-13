class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter 
        word_one = sorted(list(Counter(word1).keys()))
        word_two = sorted(list(Counter(word2).keys()))
        one = sorted(list(Counter(word1).values()))
        two = sorted(list(Counter(word2).values()))
        return (one == two and word_one == word_two)
