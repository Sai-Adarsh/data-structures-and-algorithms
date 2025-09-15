class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 1, 2, 3, 4
        # 1, 1, 2, 6

        # 1, 2, 3, 4
        # 24, 12, 4, 1

        left = [1]
        for _ in range(len(nums) - 1):
            left.append(left[-1] * nums[_])
        
        right = [1]
        for _ in range(len(nums) -1, 0, -1):
            right.append(right[-1] * nums[_])

        right = right[::-1]
        return [i * j for i, j in zip(left, right)]