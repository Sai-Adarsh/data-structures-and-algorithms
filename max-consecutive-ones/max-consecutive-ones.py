class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
    
        temp = 0
        for i in nums:
            if i == 1:
                temp += 1
            else:
                temp = 0
            max_one = max(max_one, temp)
        return max_one