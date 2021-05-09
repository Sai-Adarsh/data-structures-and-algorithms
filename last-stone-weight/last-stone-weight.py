class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        stones.sort()
        
        while True:
            if len(stones) == 1:
                break
            else:
                if len(stones) >= 2:
                    stones.append(abs(stones.pop() - stones.pop()))
                    stones.sort()
        
        return stones[0]