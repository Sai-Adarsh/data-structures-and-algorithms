class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for each in nums:
            if each not in hashMap:
                hashMap[each] = 1
            else:
                hashMap[each] += 1
        newArr = []
        for i, j in hashMap.items():
            newArr.append([i, j])

        newArr.sort(key = lambda x: x[1])
        return [newArr.pop()[0] for _ in range(k)]