class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s) // 2
        while n > 0:
​
            if s[:n] * (len(s) // len(s[:n])) == s:
                return True
            n -=1
        return False
