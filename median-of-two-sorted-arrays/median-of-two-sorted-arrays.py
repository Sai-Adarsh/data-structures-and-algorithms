class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L = nums1 + nums2
        L.sort()
        if len(L) == 1:
            return L[0] / len(L)
        if len(L) == 2:
            return (L[0] + L[1]) / 2
        if len(L) % 2 == 0:
            return (L[len(L) // 2] + L[(len(L) // 2) - 1]) / 2
        if len(L) % 2 != 0:
            return L[len(L) // 2]