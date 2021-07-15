class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr = ratings
        res = [1 for _ in range(len(arr))]

        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                if res[i] <= res[i - 1]:
                    res[i] = res[i - 1] + 1

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                if res[i] <= res[i + 1]:
                    res[i] = res[i + 1] + 1
        return (sum(res))