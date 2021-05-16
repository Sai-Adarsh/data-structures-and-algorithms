class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        # y - y1 / y2 - y1 = x - x1 / x2 - x1
        # y = 1
        # x = 1
        # xy1 = 0
        
        res = []
        for i in range(2, len(coordinates)):
            y = (coordinates[i][1] - coordinates[0][1]) * (coordinates[1][0] - coordinates[0][0])
            x = (coordinates[i][0] - coordinates[0][0]) * (coordinates[1][1] - coordinates[0][1])
            res.append(x == y)
            
        return all(res)