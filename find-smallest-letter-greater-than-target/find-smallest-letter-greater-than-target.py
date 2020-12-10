class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        left = 0
        right = len(letters) - 1
        while left < right:
            curr = left + (right - left) // 2
            if letters[curr] > target:
                right = curr
            else:
                left = curr + 1
        return letters[left] if letters[left] > target else letters[0]
