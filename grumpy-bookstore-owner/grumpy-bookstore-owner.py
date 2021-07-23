class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        
        i=0
        summ=0
        while i<len(customers):
            if grumpy[i]==0:
                summ=summ+customers[i]
                customers[i]=0
            i=i+1
        i=0
        j=0
        s=0
        maxx=-1
        while j<len(customers):
            s=s+customers[j]
            if j>=X-1:
                maxx=max(maxx,s)
                s=s-customers[i]
                i=i+1
            j=j+1
        return summ+maxx