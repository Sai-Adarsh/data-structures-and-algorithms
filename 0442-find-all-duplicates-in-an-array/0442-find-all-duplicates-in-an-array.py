class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        hashMap = {}
        res = []

        for each in nums:
            if each not in hashMap:
                hashMap[each] = 1
            else:
                hashMap[each] += 1
                if hashMap[each] > 1:
                    res.append(each)
        
        return res