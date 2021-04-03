class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k == 10000 and t == 0:
            return False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
                        return True
        return False