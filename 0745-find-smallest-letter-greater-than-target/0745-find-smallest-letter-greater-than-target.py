class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect_right(letters, target)
        if 0 <= index <= len(letters) - 1:
            return letters[index]
        return letters[0]