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
        nodes = [self.root]
        for ch in word:
            next_nodes = []
            for node in nodes:
                if ch in node.neighbors:
                    next_nodes.append(node.neighbors[ch])
                if ch == '.':
                    next_nodes.extend(node.neighbors.values())
            nodes = next_nodes
        
        for node in nodes:
            if node.end:
                return True
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)