class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        L = Counter(nums)
        print(L)
        n = len(nums)
        for i in L:
            if L[i] > n/2:
                return i
