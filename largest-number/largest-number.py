class larger(str):
    def __lt__(x, y):
        return x + y > y + x
        

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        
        nums = "".join(sorted(map(str, nums), key = larger))
        return "0" if nums == "0" * len(nums) else nums