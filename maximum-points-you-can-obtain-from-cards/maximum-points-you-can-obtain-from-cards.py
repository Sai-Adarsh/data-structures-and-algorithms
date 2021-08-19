class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
    
        n=len(cardPoints)
        ans=0
        t=n-k                      #rest of arr excluding total of  k elements from both sides
        Sum=sum(cardPoints)
        if n==k:
            return sum(cardPoints)
        preSum={-1:0}
        for i,val in enumerate(cardPoints):
            preSum[i]=preSum[i-1]+val
        for i in range(n-t+1):
            remove=preSum[i+t-1]-preSum[i-1]    #need to remove this subarray of n-k length
            ans=max(ans,Sum-remove)
        return ans