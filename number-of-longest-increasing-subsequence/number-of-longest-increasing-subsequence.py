class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        dp = [1 for i in nums]
        return_array = [1 for i in nums]
        for i in range(len(nums)):
            maxi = dp[i]
            count = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if maxi < dp[j] + 1:
                        maxi = max(maxi, dp[j] + 1)
                        count = return_array[j]
                    elif maxi == dp[j] + 1:
                        count += return_array[j]
            return_array[i] = count
            dp[i] = maxi
        maxr = max(dp)
        
        res = 0
        for i in range(len(dp)):
            if maxr == dp[i]:
                res+= return_array[i]
        return res