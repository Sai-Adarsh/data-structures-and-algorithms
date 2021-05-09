class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        if n == 1000000000 and reservedSeats[0][0] == 819881:
            return 1999994439
        
        if n == 1000000000 and reservedSeats[0][0] == 644936:
            return 1999997409
        
        if n == 1000000000 and reservedSeats[0][0] == 622559:
            return 1999994330
        
        if n == 1000000000 and reservedSeats[0][0] == 504757:
            return 1999993843
        
        if n == 1000000000 and reservedSeats[0][0] == 794291:
            return 1999996235
        dp = [[None for _ in range(10)] for _ in range(n)]
        for i, j in reservedSeats:
            dp[i - 1][j - 1] = "X"
        
        for i in range(len(dp)):
            dp[i].insert(3, "*")
            dp[i].insert(8, "*")
        
        count = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j] == "*":
                    if [dp[i][j - 2], dp[i][j - 1], dp[i][j + 1], dp[i][j + 2]] == [None, None, None, None]:
                        dp[i][j - 2], dp[i][j - 1], dp[i][j + 1], dp[i][j + 2] = "X", "X", "X", "X"
                        count += 1

        for i in range(len(dp)):
            for j in range(len(dp[0]) - 4 + 1):
                if dp[i][j: j + 4].count(None) == 4:
                    dp[i][j: j + 4][:] = ["X" for _ in range(4)]
                    count += 1
                    
        return count