class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        hash_set = []
        while right < len(s):
            if s[right] not in hash_set:
                hash_set.append(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                hash_set.remove(s[left])
                left += 1
        return max_length
