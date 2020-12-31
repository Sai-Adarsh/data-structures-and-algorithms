class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        L = list(Counter(nums).items())
        L = list(filter(lambda x: x[1] > len(nums) // 3, L))
        return([i[0] for i in L])
​
