class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        
        all_tank = 0
        # to check if round trip is possible
        # round trip is possible only if sum of all_tank >= 0
        curr_tank = 0
        # to check if at any point, we go dry
        # if so until every city until ith point isn't possible
        # let's try from i + 1, empty tank again (curr_tank) = 0
        start = 0
        # possible city
        # iterate when curr_tank goes dry
        
        
        for i in range(len(gas)):
            all_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            if curr_tank < 0:
                curr_tank = 0
                start = i + 1
                
        return start if all_tank >= 0 else -1