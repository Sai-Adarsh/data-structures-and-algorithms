class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        # generate a list of substrings or 123456789
        # from length of low to length of high loop and append sub_strings to res
        
        s = "123456789"
        L = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
        L = list(filter(lambda x: len(str(low)) <= len(x) <= len(str(high)) and low <= int(x) <= high, L))
        return sorted([int(i) for i in L])
        
        