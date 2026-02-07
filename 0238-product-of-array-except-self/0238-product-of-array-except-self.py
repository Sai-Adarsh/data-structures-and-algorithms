class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1, 2, 3, 4
        # left = [1, 1, 2, 6]
        # right = [24, 12, 4, 1]
        # 24, 12, 8, 6

        left = [1]

        for i in range(len(nums) - 1):
            left.append(left[-1] * nums[i])

        right = [1]
        for i in range(len(nums) - 1, 0, -1):
            right.append(right[-1] * nums[i])
        
        right = right[::-1]

        return [i * j for i, j in zip(left, right)]