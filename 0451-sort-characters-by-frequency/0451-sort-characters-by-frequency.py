class Solution:
    def frequencySort(self, s: str) -> str:

        hashMap = collections.Counter(s)
        L = list(map(list, hashMap.items()))
        L.sort(key=lambda x: x[1], reverse=True)
        return "".join([L[_][0] * L[_][1] for _ in range(len(L))])