nums  = [5, 3, 7, 1, 20, 9]

for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1
    while j >= 0 and key <= nums[j]:
        nums[j + 1], nums[j] = nums[j], nums[j + 1]
        j -= 1
print(nums)
