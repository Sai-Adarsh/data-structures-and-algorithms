class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        S = [str(i) for i in S]
        count = 0
        for i in range(0, len(S)):
            if S[i] in J:
                count+=1
        return count
