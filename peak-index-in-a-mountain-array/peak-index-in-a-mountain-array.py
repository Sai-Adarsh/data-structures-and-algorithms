class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
​
        left = 0
        right = len(A) - 1
        while left < right:
            curr = left + (right - left) // 2
            if A[curr] < A[curr + 1]:
                left = curr + 1
            else:
                right = curr
        return left
