class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        hashMap = collections.Counter(nums)
        count = 0

        if k == 0:
            for val in hashMap:
                if hashMap[val] > 1:
                    count += 1
        else:
            for eachNum in hashMap:
                if k + eachNum in hashMap:
                    count += 1

        return count