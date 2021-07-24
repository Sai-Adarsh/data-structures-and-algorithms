class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        
        
        # stack approach
        # put string, cost in stack, if last two same, pop min, res += min's cost
        s = [(s[i], cost[i]) for i in range(len(s))]
        
        stack = []
        res = 0
        
        for i, j in s:
            stack.append((i, j))
            if len(stack) >= 2:
                if stack[-2][0] == stack[-1][0]:
                    if stack[-2][1] < stack[-1][1]:
                        res += stack[-2][1]
                        del stack[len(stack) - 2]
                    else:
                        res += stack[-1][1]
                        del stack[len(stack) - 1]
                    
        return res