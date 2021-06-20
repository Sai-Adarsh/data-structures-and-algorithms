class TrieNode:
    
    def __init__(self):
        self.end = False
        self.neighbors = {}

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        root = self.root
        
        for i in word:
            if i not in root.neighbors:
                root.neighbors[i] = TrieNode()
            root = root.neighbors[i]
        root.end = True
        

    def search(self, word: str) -> bool:
        root = self.root
        
        def backTracking(word, root):
            if not word:
                return root.end
            
            if word[0] == ".":
                return any(backTracking(word[1:], i) for i in root.neighbors.values())
            
            if word[0] not in root.neighbors:
                return False
            
            return backTracking(word[1:], root.neighbors[word[0]])
        
        return backTracking(word, root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)