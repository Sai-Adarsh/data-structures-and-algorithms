class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hashMap = collections.Counter(nums)

        targetFreq = len(nums) // 3
        res = []
        for i, j in hashMap.items():
            if j > targetFreq:
                res.append(i)

        return res