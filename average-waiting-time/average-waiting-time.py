class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        
        # bruteforce approach
        # res = 0
        # if i == 0, start, end. end = end + start, res += end - start
        # else, [i][1] = [i][1] + [i - 1][1], res += end - start
        
        res = 0
        for i in range(len(customers)):
            if i == 0:
                customers[i][1] += customers[i][0]
                res += customers[i][1] - customers[i][0]
            else:
                if customers[i - 1][1] > customers[i][0]:
                    customers[i][1] += customers[i - 1][1]
                else:
                    customers[i][1] += customers[i][0]
                res += customers[i][1] - customers[i][0]
                
        return res / len(customers)