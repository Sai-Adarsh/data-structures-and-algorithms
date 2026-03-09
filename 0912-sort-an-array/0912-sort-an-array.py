class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        heapq.heapify(nums)

        res = []
        while nums:
            res.append(heapq.heappop(nums))
        
        return res