class Solution:
    def countPrimes(self, n: int) -> int:
        
        
        def SOE(n):
            if n == 0:
                return []
            seive = [True for _ in range(n + 1)]
            seive[0] = False
            seive[1] = False
            
            for i in range(2, int(math.sqrt(n)) + 1):
                if seive[i] == False:
                    continue
                for pointer in range(i * i, n + 1, i):
                    seive[pointer] = False
                    
            primes = []
            for i in range(n):
                if seive[i] == True:
                    primes.append(i)
                    
            return primes
        
        return len(SOE(n))