class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        
        res = []
        L = []
        heapq.heapify(L)
        
        
        
        for i in range(len(nums)):
            bisect.insort(L, nums[i])
            
            
            if len(L) >= k:
                if k % 2 != 0:
                    res.append(L[len(L) // 2])
                else:
                    res.append((L[len(L) // 2] + L[(len(L) // 2) - 1]) / 2)
                L.remove(nums[i - k + 1])
        return res