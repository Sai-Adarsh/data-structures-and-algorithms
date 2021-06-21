class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        L = list(map(list, collections.Counter(nums).items()))
        L.sort(key = lambda x: x[1])
        return L[0][0]