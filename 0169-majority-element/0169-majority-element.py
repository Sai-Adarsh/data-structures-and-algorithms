class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashMap = collections.Counter(nums)
        n = len(nums)
        for k, v in hashMap.items():
            if v > n // 2:
                return k