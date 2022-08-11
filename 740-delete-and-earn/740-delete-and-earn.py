class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        dic = collections.Counter(nums)
        keys = sorted(dic.keys())
        prev = 0
        curr = keys[0]*dic[keys[0]]
        for i in range(1, len(keys)):
            if keys[i] - keys[i-1] == 1:
                prev, curr = curr, max(prev + keys[i] * dic[keys[i]], curr)
            else:
                prev, curr = curr, curr + keys[i] * dic[keys[i]]
        return curr