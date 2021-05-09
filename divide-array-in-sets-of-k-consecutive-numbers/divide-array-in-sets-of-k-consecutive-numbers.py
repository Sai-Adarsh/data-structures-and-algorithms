class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        splitter = len(nums) // k
        
        nums.sort()
        res = []
        
        hash_map = collections.Counter(nums)
        
        i = 0
        while i < splitter:
            L = []
            list_version_of_map = list(map(list, hash_map.items()))
            for _ in range(len(list_version_of_map) - 1, len(list_version_of_map) - k - 1, -1):
                temp = list_version_of_map[_]
                L.append(temp[0])
                if len(L) >= 2:
                    if abs(L[-1] - L[-2]) != 1:
                        return False
                hash_map[temp[0]] -= 1
                if hash_map[temp[0]] == 0:
                    del hash_map[temp[0]]
            res.append(L)
            i += 1
            
        if sum(len(i) for i in res) == len(nums):
            return True
        return False