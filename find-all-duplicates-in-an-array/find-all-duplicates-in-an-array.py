class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash_set = {}
        res = []
        for i in nums:
            if i not in hash_set:
                hash_set[i] = i
            else:
                res.append(i)
        return res
