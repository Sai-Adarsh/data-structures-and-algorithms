class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashMap = collections.Counter()

        left = 0
        right = 0
        res = 0

        while right <= len(s) - 1:
            hashMap[s[right]] += 1
            
            while True:
                if hashMap[s[right]] == 1:
                    break
                else:
                    hashMap[s[left]] -= 1
                    left += 1
            res = max(res, right - left + 1)
            right += 1

        return res