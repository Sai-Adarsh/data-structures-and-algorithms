class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = []
        one = []
        two = []
        
        for i in nums:
            if i == 0:
                zero.append(0)
            elif i == 1:
                one.append(1)
            else:
                two.append(2)
                
        nums[:] = zero + one + two