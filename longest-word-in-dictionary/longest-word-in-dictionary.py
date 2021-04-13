class Solution:
    def longestWord(self, words: List[str]) -> str:
        wordset = set(words)
        words.sort(key = lambda c: (-len(c), c))
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word

        return ""