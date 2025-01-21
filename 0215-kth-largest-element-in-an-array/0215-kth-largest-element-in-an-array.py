class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        nums.sort(reverse = True)

        for _ in range(k):
            if _ == k - 1:
                return nums.pop(0)
            nums.pop(0)