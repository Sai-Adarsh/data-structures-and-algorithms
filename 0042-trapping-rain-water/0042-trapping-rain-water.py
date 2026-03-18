class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0]]
        for i in range(1, len(height)):
            left.append(height[i] if height[i] > left[-1] else left[-1])
        right = [height[-1]]
        for j in range(len(height) - 2, -1, -1):
            right.append(height[j] if height[j] > right[-1] else right[-1])
        right = right[::-1]
        res = 0
        for i in range(len(height)):
            currMin = min(left[i], right[i])
            if currMin > height[i]:
                res += (currMin - height[i])
        return res