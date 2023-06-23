class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]

        one = nums[1:]
        two = nums[:-1]

        if len(one) == 1 and len(two) == 1:
            return max(one[-1], two[-1])

        dpOne = [one[0], max(one[0], one[1])]
        dpTwo = [two[0], max(two[0], two[1])]

        for i in range(2, len(one)):
            dpOne.append(max(one[i] + dpOne[-2], dpOne[-1]))
        
        for j in range(2, len(two)):
            dpTwo.append(max(two[j] + dpTwo[-2], dpTwo[-1]))

        print(one, two)
        print(dpOne, dpTwo)

        return max(dpOne[-1], dpTwo[-1])