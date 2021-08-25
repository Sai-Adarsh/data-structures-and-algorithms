class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        # Naive brute force approach
        # Comprehend both the arrays
        # if len == odd, return middle
        # if len == even, return (middle - 1 + middle) / 2
        
        nums1[:] = nums1 + nums2
        nums1.sort()
        curr_len = len(nums1)
        
        if curr_len % 2 != 0:
            return nums1[curr_len // 2]
        else:
            return (nums1[curr_len // 2] + nums1[(curr_len // 2) - 1]) / 2