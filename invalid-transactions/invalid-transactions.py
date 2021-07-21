class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        t = transactions
        t = [x.split(",")+[False] for x in t]
        
        for pos, order in enumerate(t):
        
            name, time, amount, city, isValid = order
            
            for prev in range(pos):
                
                if t[prev][0] == name and abs(int(time)-int(t[prev][1])) <= 60 and t[prev][3] != city:
                    t[prev][-1] = True
                    order[-1] = True
        
            if order[-1] == False and int(amount) > 1000:
                order[-1] = True
            
        res = []
        
        for x in t:
            if x[-1] == True:
                res.append(",".join(x[:-1]))
        return res