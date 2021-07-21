class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        queue = []
        val = 0
        for i in range(n):
            maxV = 0
            if queue:
                maxV, indx = queue[0]
                while indx+k < i:
                    maxV, indx = heapq.heappop(queue)
                heapq.heappush(queue, [maxV,indx])
            val = nums[i] + (-1) * maxV
            heapq.heappush(queue, [-1 * val, i]) 
        return val