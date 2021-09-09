class Solution:
    def minOperations(self, s: str) -> int:
        
        n = len(s)
        
        one = ""
        while True:
            if len(one) >= n:
                break
            else:
                one += "1"
                one += "0"
        one = one[:len(s)]
                
        two = ""
        while True:
            if len(two) >= n:
                break
            else:
                two += "0"
                two += "1"
                
        two = two[:len(s)] 
            
        count_one = 0
        for i, j in zip(s, one):
            if i != j:
                count_one += 1
                
                
        count_two = 0
        for i, j in zip(s, two):
            if i != j:
                count_two += 1
        
        return min(count_one, count_two)