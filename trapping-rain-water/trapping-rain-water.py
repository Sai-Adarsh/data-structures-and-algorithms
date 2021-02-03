class Solution:
    def trap(self, height: List[int]) -> int:
        i = 1
        res = 0
        while i < len(height) - 1:
            L = min(max(height[:i]), max(height[i + 1:])) - height[i]
            if L >= 0:
                res += L
            i += 1
        return res