class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        temp = left
        left = 0
        right = len(nums) - 1

        if target >= nums[temp] and target <= nums[right]:
            left = temp
        else:
            right = temp
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right -= 1
            else:
                left += 1
        return -1