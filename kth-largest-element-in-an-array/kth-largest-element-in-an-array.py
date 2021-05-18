class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        res = []
        heapq.heapify(res)
        
        for i in nums:
            heapq.heappush(res, i)
            
        for _ in range(len(nums) - k):
            heapq.heappop(res)
            
        return res.pop(0)