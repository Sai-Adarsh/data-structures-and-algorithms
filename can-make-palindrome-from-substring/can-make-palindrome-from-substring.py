class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for c in s: 
            prefix.append(prefix[-1] ^ (1 << (ord(c)-97)))
        
        ans = []
        for left, right, k in queries: 
            cnt = bin(prefix[right+1] ^ prefix[left]).count("1")
            ans.append(cnt <= 2*k+1)
        return ans 