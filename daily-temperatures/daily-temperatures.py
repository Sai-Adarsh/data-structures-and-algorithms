class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        
        stack = []
        output_arr = [0 for _ in range(len(T))]
        
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                temp = stack.pop()
                output_arr[temp] = i - temp
            
            stack.append(i)
            
        return output_arr
            
        