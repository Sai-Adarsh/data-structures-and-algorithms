class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for i in word:
            if i not in root.children:
                root.children[i] = TrieNode()
            root = root.children[i]
        root.isEnd = True

    def search(self, word: str) -> bool:
        root = self.root
        for i in word:
            if i not in root.children:
                return False
            root = root.children[i]
        return root.isEnd == True

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for i in word:
            if i not in root.children:
                return False
            root = root.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)