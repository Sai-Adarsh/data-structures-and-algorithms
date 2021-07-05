# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n - 1
        
        while left <= right:
            curr = left + (right - left) // 2
            if not isBadVersion(curr):
                left = curr + 1
            else:
                right = curr - 1
        return left