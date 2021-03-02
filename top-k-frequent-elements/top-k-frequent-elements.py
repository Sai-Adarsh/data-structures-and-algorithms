class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        L = list(map(list, Counter(nums).items()))
        L.sort(key = lambda x: x[1], reverse = True)
        return [i[0] for i in L][:k]