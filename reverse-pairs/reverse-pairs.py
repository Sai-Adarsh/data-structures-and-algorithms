class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        arr = []
        res = 0
        for each_num in nums:
            index = bisect.bisect_right(arr, each_num * 2)
            res += len(arr) - index
            bisect.insort(arr, each_num)
            
        return res