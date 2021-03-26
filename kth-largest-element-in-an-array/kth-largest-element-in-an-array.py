class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq
        L = heapq.heapify(nums)
        
        return heapq.nlargest(k, nums)[-1]