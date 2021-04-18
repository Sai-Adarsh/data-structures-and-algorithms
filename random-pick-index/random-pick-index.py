class Solution:

    def __init__(self, nums: List[int]):
        
        self.nums = nums
        self.adjacency_list = {}

    def pick(self, target: int) -> int:
        
        for i in range(len(self.nums)):
            if self.nums[i] not in self.adjacency_list:
                self.adjacency_list[self.nums[i]] = [i]
            else:
                self.adjacency_list[self.nums[i]].append(i)
                
        return random.choice(self.adjacency_list[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)