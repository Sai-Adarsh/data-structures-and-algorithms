class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        table = {}
        
        for i in range(len(S)):
            table[S[i]] = i
            
        start = 0
        end = 0
        
        res = []
        for i in range(len(S)):
            # for us to find where to partition, we've to know the farthest occurence of a word
            end = max(end, table[S[i]])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        
        return res