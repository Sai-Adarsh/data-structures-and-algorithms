class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = [i for i in s]
        result = [None for _ in range(len(s)) ]
        for i in range(len(s)):
            result[indices[i]] = s[i]
        return("".join(result))
