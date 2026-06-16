class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        allList = [_ for _ in range(1, n + 1)]

        def backTracking(currArr, finalArr, j):
            if len(currArr) == k:
                finalArr.append(currArr)
                return

            for i in range(j, len(allList)):
                if allList[i] not in currArr:
                    backTracking(currArr + [allList[i]], finalArr, i + 1)
            
            return finalArr

        return backTracking([], [], 0)