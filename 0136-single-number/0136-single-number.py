class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = collections.Counter(nums)

        for i, j in hashMap.items():
            if j != 2:
                return i