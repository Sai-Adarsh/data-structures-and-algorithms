class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []
        for i in points:
            res.append([i, abs(i[0] ** 2) + abs(i[1] ** 2)])
        res.sort(key = lambda x: x[1])
        res = [i[0] for i in res]
        return(res[:K])