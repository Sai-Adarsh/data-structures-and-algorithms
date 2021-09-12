class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        hash_map = {}
        res = 0
        for i in nums1:
            for j in nums2:
                if i + j not in hash_map:
                    hash_map[i + j] = 1
                else:
                    hash_map[i + j] += 1
        
        for i in nums3:
            for j in nums4:
                target = -(i + j)
                if target in hash_map:
                    res += hash_map[target]
        return res