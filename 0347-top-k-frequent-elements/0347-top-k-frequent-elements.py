class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashMap = collections.Counter(nums)
        res = list(map(tuple, hashMap.items()))
        res.sort(key = lambda x: x[1])
        final = []
        for i in range(k):
            final.append(res.pop()[0])
        return final