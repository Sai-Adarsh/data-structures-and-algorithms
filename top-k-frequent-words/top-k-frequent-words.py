class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        master = Counter(words)
        L = list(Counter(words).items())
        L.sort(key = lambda x: (x[1], x[0]), reverse = True)
        nums = [i[0] for i in L]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if master[nums[i]] == master[nums[j]]:
                    nums[i], nums[j] = min(nums[i], nums[j]), max(nums[i], nums[j])
        return nums[:k]
        