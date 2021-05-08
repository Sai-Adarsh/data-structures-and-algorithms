class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        all_tank = 0
        curr_tank = 0
        start = 0
        for i in range(len(gas)):
            all_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            if curr_tank < 0:
                curr_tank = 0
                start = i + 1
                
            
        return start if all_tank >= 0 else -1