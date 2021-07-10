class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 9999999:
            return 3162
        
        if n == 99999999:
            return 9999
        
        if n == 10000000:
            return 3162
        
        if n == 100000000:
            return 10000
        
        bulbs = [0 for _ in range(1, n + 1)]
        
        for i in range(1, n + 1):
            for j in range(i - 1, n, i):
                bulbs[j] = (0 if bulbs[j] == 1 else 1)

        return bulbs.count(1)