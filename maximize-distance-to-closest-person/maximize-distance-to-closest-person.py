class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        
        # Normal
        
        res = 0
        temp = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                res = max(res, math.ceil(temp / 2))
                temp = 0
            else:
                temp += 1
                
        res = max(res, math.ceil(temp / 2))
            
        
        one = 0
        i = 0
        while True:
            if seats[i] == 1:
                break
            else:
                one += 1
                i += 1
                
        seats[:] = seats[::-1]
        res = max(res, one)
        
        one = 0
        i = 0
        while True:
            if seats[i] == 1:
                break
            else:
                one += 1
                i += 1
                
        res = max(res, one)
        
        return res