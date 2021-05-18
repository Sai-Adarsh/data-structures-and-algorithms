class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        
        L = list(map(list, itertools.product(nums1, nums2)))
        L.sort(key = lambda x: sum(x))
        
        if len(L) <= k:
            return L
        res = [L.pop(0) for _ in range(k)]
        return res