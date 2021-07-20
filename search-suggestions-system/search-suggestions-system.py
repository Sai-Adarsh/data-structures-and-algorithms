class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        
        products.sort()
        res = []
        for i in range(len(searchWord)):
            temp = searchWord[: i + 1]
            L = []
            for j in range(len(products)):
                prefix = products[j][: i + 1]
                if temp == prefix:
                    if len(L) <= 2:
                        L.append(products[j])
            res.append(L)
            
        return res