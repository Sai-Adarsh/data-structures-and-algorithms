class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        L = [i for i in range(1, n + 1)]
        L.sort(key = lambda x: str(x))
        return L