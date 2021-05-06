class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()
        
        while True:
            if len(stones) == 1:
                break
            else:
                if len(stones) >= 2:
                    stones.append(stones.pop() - stones.pop())
                    stones.sort()
                    print(stones)
                else:
                    break
                    
        return stones[0]