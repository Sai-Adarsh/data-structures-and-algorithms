class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
​
class Trie:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
​
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True
        
​
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.end == True
        
​
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        curr = self.root
        for i in prefix:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return True
​
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
