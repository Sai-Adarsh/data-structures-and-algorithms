class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        return int(numBottles + (numBottles - 1) / (numExchange - 1))