class Solution:
    def numWays(self, s: str) -> int:
        
        ones=[i for i,c in enumerate(s) if c=='1']
        l,l_ones=len(s),len(ones)
        if l_ones%3!=0:
            return 0
        elif not l_ones:
            return int((((l-2)*(l-1))/2)%(1e9+7))
        elif l_ones==l:
            return 1
        exp=l_ones//3
        return int(((ones[exp*1]-ones[exp*1-1]) * (ones[exp*2]-ones[exp*2-1]))%(1e9+7))