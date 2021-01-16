class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        memo = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        L = product(*[tuple(x for x in memo[i]) for i in digits])
        return(list(map(''.join, L)))
            
