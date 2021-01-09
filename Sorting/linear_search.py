nums  = [5, 3, 7, 1, 20, 9]

for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)