class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0]]

        for i in range(1, len(height)):
            if height[i] > left[-1]:
                left.append(height[i])
            else:
                left.append(left[-1])

        right = [height[-1]]

        for i in range(len(height) - 2, -1, -1):
            if height[i] > right[-1]:
                right.append(height[i])
            else:
                right.append(right[-1])
        
        right = right[::-1]

        res = 0
        for i in range(len(height)):
            if i == 4:
                print(left, right, height[i])
            currMin = min(left[i], right[i])
            if currMin - height[i] > 0:
                res += (currMin - height[i])
        
        return res