class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}
        

    def buildDict(self, dictionary: List[str]) -> None:
        for each in dictionary:
            self.hash_map[each] = each
        
        
    def search(self, searchWord: str) -> bool:
        for each in self.hash_map.values():
            if len(each) == len(searchWord):
                count = 0
                for i, j in zip(each, searchWord):
                    if i != j:
                        count += 1
                if count == 1:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)