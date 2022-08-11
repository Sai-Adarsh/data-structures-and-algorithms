class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        The problem can be reduced to Problem 198. House Robber. Let minimum (maximum) be the minimum (maximum) of nums, and let dic be a Hash map counting the number of occurences of each number in [minimum, maximum]. Denote by F(i) the maximum number of points that one can earn with numbers in the range[minimum, i]. Then we have the recursive relation F(i) = max(F(i-2)+ dic[i] * i, F(i-1)). By iterating i over [minimum, maximum] and each time updating F(i-1) and F(i) with the recursive formula, one can easily get F(maximum), the maximum number of points that one can earn with numbers in the range [minimum, maximum], which is the desired value of the solution.

        Time complexity O(n+m), where n = len(nums) and m = range of number in nums. Space complexity O(m).

        class Solution:
            def deleteAndEarn(self, nums):

                if not nums:
                    return 0
                dic = collections.defaultdict(int)
                minimum = float('inf')
                maximum = -float('inf')
                for n in nums:
                    dic[n] += 1
                    maximum = max(maximum, n)
                    minimum = min(minimum, n)
                prev = 0
                curr = 0
                for i in range(minimum, maximum+1):
                    prev, curr = curr, max(prev + dic[i]*i, curr)
                return curr

        Caveat: According to the problem description, the length of nums is at most 20000, and each element nums[i] is an integer in the range [1, 10000]. Therefore, the above algorithm runs in O(n) time. However, one can image a scenario where the range of numbers in nums is much larger than n. Then the above algorithm is not optimal, and one should use the algorithm below, which runs in O(n log n) time and has space complexity O(n).

        class Solution(object):
            def deleteAndEarn(self, nums):
                if not nums:
                    return 0
                dic = collections.Counter(nums)
                keys = sorted(dic.keys())
                prev = 0
                curr = keys[0]*dic[keys[0]]
                for i in range(1, len(keys)):
                    if keys[i] - keys[i-1] == 1:
                        prev, curr = curr, max(prev + keys[i] * dic[keys[i]], curr)
                    else:
                        prev, curr = curr, curr + keys[i] * dic[keys[i]]
                return curr
        """
        if not nums:
            return 0
        dic = collections.defaultdict(int)
        minimum = float('inf')
        maximum = -float('inf')
        for n in nums:
            dic[n] += 1
            maximum = max(maximum, n)
            minimum = min(minimum, n)
        prev = 0
        curr = 0
        print(maximum, minimum)
        for i in range(minimum, maximum+1):
            prev, curr = curr, max(prev + dic[i]*i, curr)
        return curr