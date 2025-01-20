class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L = list(map(list, collections.Counter(nums).items()))
        L.sort(key = lambda x: x[1])
        return [L.pop()[0] for _ in range(k)]