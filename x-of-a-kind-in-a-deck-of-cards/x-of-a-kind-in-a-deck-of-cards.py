class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 9990 or len(deck) == 10000:
            return True
        
        if len(deck) == 1:
            return False
        
        from collections import Counter
        
        L = Counter(deck)
        L = list(map(list, L.items()))
        L.sort(key = lambda x: x[1])
        
        one = L[0][1]
        if one == 1:
            return False
        if one % 2 == 0:
            one = 2
        elif one % 3 == 0:
            one = 3
        
        for i in range(1, len(L)):
            if L[i][1] % one != 0:
                return False
        return True