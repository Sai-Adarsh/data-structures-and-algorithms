class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        master = [[1], [1, 1]]
        
        if numRows == 1:
            return [master[0]]
        if numRows == 2:
            return master
        
        for i in range(numRows - 2):
            temp = []
            for _ in range(len(master[-1]) + 1):
                if _ == 0 or _ == len(master[-1]):
                    temp.append(1)
                else:
                    temp.append(master[-1][_] + master[-1][_ - 1])
            master.append(temp)
            
        return master