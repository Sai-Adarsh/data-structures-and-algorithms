class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        heapq.heapify(nums)
        res = []

        while nums:
            res.append(heapq.heappop(nums))

        nums[:] = res