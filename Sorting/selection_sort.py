nums  = [5, 3, 7, 1, 20, 9]

for i in range(len(nums)):

    min_index = i
    for j in range(i, len(nums)):
        if nums[j] < nums[min_index]:
            min_index = j
    nums[min_index], nums[i] = nums[i], nums[min_index]
print(nums)