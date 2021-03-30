class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        from collections import Counter
        L = list(map(list, Counter(nums).items()))
        L = list(filter(lambda x: x[1] > len(nums) // 2, L))
        return L[0][0]