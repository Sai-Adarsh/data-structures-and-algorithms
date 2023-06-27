class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0 
        right = 0
        res = 0
        hashMap = collections.Counter()
        maxCount = 0

        while right <= len(s) - 1:
            hashMap[s[right]] += 1
            maxCount = max(maxCount, hashMap[s[right]])

            while (right - left + 1) - maxCount > k:
                hashMap[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1

        return res