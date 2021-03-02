class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from itertools import product
        L = list(map(list, product(tuple(nums1), tuple(nums2))))
        L.sort(key = lambda x: sum(x))
        return L[:k]