# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            curr = left + (right - left) // 2
            if guess(curr) == 0:
                return curr
            elif guess(curr) == 1:
                left = curr + 1
            else:
                right = curr - 1