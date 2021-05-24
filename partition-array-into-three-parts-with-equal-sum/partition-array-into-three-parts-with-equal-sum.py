class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        
        
        total = sum(arr)
        curr_sum = 0
        count = 0
        
        if total % 3 != 0:
            return False
        
        for i in arr:
            curr_sum += i
            if curr_sum == total // 3:
                curr_sum = 0
                count += 1
                
        if count >= 3:
            return True
        return False
        