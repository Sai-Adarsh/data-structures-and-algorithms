class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        L = Counter(nums)
        n = len(nums)
        res = []
        for i in L:
            if L[i] > n/3:
                res.append(i)
        return res
